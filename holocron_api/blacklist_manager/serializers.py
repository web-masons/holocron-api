from rest_framework import serializers
from blacklist_manager.models import BlacklistEntry, Entries  # noqa
import re

ipv6_regex = re.compile('(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,6}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,6}(:[0-9a-f]{1,4}){1,1}\Z)|'
                        '(\A(([0-9a-f]{1,4}:){1,7}|:):\Z)|'
                        '(\A:(:[0-9a-f]{1,4}){1,7}\Z)|'
                        '(\A((([0-9a-f]{1,4}:){6})(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d)'
                        '(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
                        '(\A(([0-9a-f]{1,4}:){5}[0-9a-f]{1,4}:'
                        '(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d))'
                        '{3})\Z)|'
                        '(\A([0-9a-f]{1,4}:){5}:[0-9a-f]{1,4}:'
                        '(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d))'
                        '{3}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,4}:(25'
                        '[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.'
                        '(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,3}:(25'
                        '[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.'
                        '(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,2}:(25'
                        '[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d))'
                        '{3}\Z)|'
                        '(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,1}:(25['
                        '0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d))'
                        '{3}\Z)|'
                        '(\A(([0-9a-f]{1,4}:){1,5}|:):(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d)'
                        '(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
                        '(\A:(:[0-9a-f]{1,4}){1,5}:(25[0-5]|2[0-4]\d|'
                        '[0-1]?\d?\d)'
                        '(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)')

ipv4_regex = re.compile('^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|'
                        '1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]'
                        '\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$')

ipv4_cidr_regex = re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|'
                             '25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2'
                             '[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3['

                             '0-2]))$')


class BlacklistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlacklistEntry
        fields = ('id', 'entry_type', 'entry', 'description', 'added_by')

    def validate(self, data):
        if data['entry_type'] is BlacklistEntry.IP_ADDRESS:
            if not ipv4_regex.match(data['entry']) and \
                    not ipv6_regex.match(data['entry']):
                raise serializers.ValidationError("IP Address is not Valid.  "
                                                  "Please enter a IPv4 or "
                                                  "IPv6 address.")
        if data['entry_type'] is BlacklistEntry.IP_RANGE:
            if not ipv4_cidr_regex.match(data['entry']):
                raise serializers.ValidationError("IP Address Range is not "
                                                  "Valid.  Please enter a "
                                                  "IPv4 CIDR.")
                # limit to /25 - /32 to only update last octet
            cidr = data['entry'].split("/")
            cidr = int(cidr[-1])
            if cidr < 25:
                raise serializers.ValidationError("Range is too large.  "
                                                  "Limit range to last "
                                                  "octet.")
        return data


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
