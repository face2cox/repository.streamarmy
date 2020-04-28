# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMjIyMjIyMjIyMjI0NPREUgQlkgQE5FTVpaWTY2OCMjIyMjIyMjIyMjDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQppbXBvcnQgeGJtYyx4Ym1jYWRkb24seGJtY2d1aSx4Ym1jcGx1Z2luLHVybGxpYix1cmxsaWIyLG9zLHJlLHN5cyxiYXNlNjQsanNvbix0aW1lLHJlcXVlc3RzLHJlc29sdmV1cmwNCmZyb20gcmVzb3VyY2VzLmxpYnMuY29tbW9uX2FkZG9uIGltcG9ydCBBZGRvbg0KZnJvbSByZXNvdXJjZXMubGlicy5tb2R1bGVzIGltcG9ydCB3b3JrZXJzDQpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQ0KZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXANCnJlbG9hZChzeXMpDQpzeXMuc2V0ZGVmYXVsdGVuY29kaW5nKCJ1dGYtOCIpDQoNCg0KYWRkb25faWQgICAgICAgICAgICA9ICdwbHVnaW4udmlkZW8uYXBvY2FseXBzZTcyMCcNCmFkZG9uICAgICAgICAgICAgICAgPSBBZGRvbihhZGRvbl9pZCwgc3lzLmFyZ3YpDQpiYXNldXJsICAgICAgICAgICAgID0gYmFzZTY0LmI2NGRlY29kZShiJ2FIUjBjRG92TDI1dmJHVmtlVzVoYzNSNUxuaDVlaTlqYVc1bGJXRXZZMmx1WlcxaGJXRnBiaTU0Yld3PScpDQpzZWxmQWRkb24gICAgICAgICAgID0geGJtY2FkZG9uLkFkZG9uKGlkPWFkZG9uX2lkKQ0KQWRkb25UaXRsZSAgICAgICAgICA9ICdbQ09MT1IgZ29sZF1bQl1BcG9jYWx5cHNlIDcyMFsvQl1bL0NPTE9SXScNCmFkZG9uUGF0aCAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4ob3MucGF0aC5qb2luKHhibWMudHJhbnNsYXRlUGF0aCgnc3BlY2lhbDovL2hvbWUnKSwgJ2FkZG9ucycpLCdwbHVnaW4udmlkZW8uYXBvY2FseXBzZTcyMCcpDQpmYW5hcnRzICAgICAgICAgICAgID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBhZGRvbl9pZCwgJ2ZhbmFydC5qcGcnKSkNCmZhbmFydCAgICAgICAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIGFkZG9uX2lkLCAnZmFuYXJ0LmpwZycpKQ0KaWNvbiAgICAgICAgICAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgYWRkb25faWQsICdpY29uLnBuZycpKQ0KU2ljb24gICAgICAgICAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgYWRkb25faWQsICdTZWFyY2gucG5nJykpDQpBZGRvbmljb24gICAgICAgICAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIGFkZG9uX2lkLCAnaWNvbi5wbmcnKSkNCmRwICAgICAgICAgICAgICAgICAgPSB4Ym1jZ3VpLkRpYWxvZ1Byb2dyZXNzKCkNCmRpYWxvZyAgICAgICAgICAgICAgPSB4Ym1jZ3VpLkRpYWxvZygpDQpDdXJyZW50X0Rvd25sb2FkcyAgID0gICcnDQptZXNzYWdldGV4dCAgICAgICAgID0gJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy8wdGh6OWlORycNCnlvdXR1YmVhcGkgICAgICAgICAgPSBiYXNlNjQuYjY0ZGVjb2RlKGInUVVsNllWTjVRVEl3ZVV4MVQyRmFaV1ZOVUcxTVpGWTVTREpNYVVoSlYwRndNbXhHWVdaaicpDQp0bWRiYXBpICAgICAgICAgICAgID0gYmFzZTY0LmI2NGRlY29kZShiJ05URXpOVE16TkdSaFlUTXpNalV4WW1NME1EZGxOV1l5TkdOaU1XTTJZVFU9JykNCg0KZGVmIHBvcHVwKCk6DQoNCgltZXNzYWdlPSBvcGVuX21zZyhtZXNzYWdldGV4dCkNCglpZiBsZW4obWVzc2FnZSk+MToNCgkJcGF0aCA9IHhibWNhZGRvbi5BZGRvbigpLmdldEFkZG9uSW5mbygncGF0aCcpDQoJCWNvbXBhcmVmaWxlID0gb3MucGF0aC5qb2luKG9zLnBhdGguam9pbihwYXRoLCcnKSwgJ2NvbXBhcmUudHh0JykNCgkJciA9IG9wZW4oY29tcGFyZWZpbGUpDQoJCWNvbXBmaWxlID0gci5yZWFkKCkgICAgICAgDQoJCWlmIGNvbXBmaWxlID09IG1lc3NhZ2U6cGFzcw0KCQllbHNlOg0KCQkJc2hvd1RleHQoJ1tDT0xPUiBnb2xkXVtCXUFwb2NhbHlwc2UgNzIwIEluZm9ybWF0aW9uWy9CXVsvQ09MT1JdJywgbWVzc2FnZSkNCgkJCXRleHRfZmlsZSA9IG9wZW4oY29tcGFyZWZpbGUsICJ3IikNCgkJCXRleHRfZmlsZS53cml0ZShtZXNzYWdlKQ0KCQkJdGV4dF9maWxlLmNsb3NlKCkNCg0KZGVmIG9wZW5fbXNnKHVybCk6DQoJdHJ5Og0KCQlyZXEgPSB1cmxsaWIyLlJlcXVlc3QodXJsKQ0KCQlyZXEuYWRkX2hlYWRlcignVXNlci1BZ2VudCcsICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzQ3LjAuMjUyNi43MyBTYWZhcmkvNTM3LjM2JykNCgkJcmVzcG9uc2UgPSB1cmxsaWIyLnVybG9wZW4ocmVxLCB0aW1lb3V0PTUpDQoJCWxpbms9cmVzcG9uc2UucmVhZCgpDQoJCXJlc3BvbnNlLmNsb3NlKCkNCgkJcmV0dXJuIGxpbmsNCglleGNlcHQ6cXVpdCgpDQoJDQpkZWYgT3BlbkxpbmsodXJsKToNCg0KCWxpbmsgPSByZXF1ZXN0cy5nZXQodXJsKS5jb250ZW50DQoJcmV0dXJuIGxpbmsNCg0KZGVmIFNFVF9WSUVXKCk6DQoNCiAgICB4Ym1jX3ZlcnNpb249eGJtYy5nZXRJbmZvTGFiZWwoIlN5c3RlbS5CdWlsZFZlcnNpb24iKQ0KICAgIHZlcnNpb249ZmxvYXQoeGJtY192ZXJzaW9uWzo0XSkNCiAgICBpZiB2ZXJzaW9uID49IDE2LjAgYW5kIHZlcnNpb24gPD0gMTYuOToNCiAgICAgICAgY29kZW5hbWUgPSAnSmFydmlzJw0KICAgIGVsaWYgdmVyc2lvbiA+PSAxNy4wIGFuZCB2ZXJzaW9uIDw9IDE3Ljk6DQogICAgICAgIGNvZGVuYW1lID0gJ0tyeXB0b24nDQogICAgZWxpZiB2ZXJzaW9uID49IDE4LjAgYW5kIHZlcnNpb24gPD0gMTguOToNCiAgICAgICAgY29kZW5hbWUgPSAnTGVpYScNCiAgICBlbHNlOiBjb2RlbmFtZSA9ICJEZWNsaW5lIg0KICAgIA0KICAgIGlmIGNvZGVuYW1lID09ICJKYXJ2aXMiOg0KICAgICAgICB4Ym1jLmV4ZWN1dGVidWlsdGluKCdDb250YWluZXIuU2V0Vmlld01vZGUoNTApJykNCiAgICBlbGlmIGNvZGVuYW1lID09ICJLcnlwdG9uIjoNCiAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlNldFZpZXdNb2RlKDU1KScpDQogICAgZWxpZiBjb2RlbmFtZSA9PSAiTGVpYSI6DQogICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5TZXRWaWV3TW9kZSg1NSknKQ0KICAgIGVsc2U6IHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5TZXRWaWV3TW9kZSg1MCknKQ0KDQpkZWYgSW5kZXhlcihuYW1lLHVybCxpY29uaW1hZ2UsZmFuYXJ0LGRlc2NyaXB0aW9uKToNCglpZiAnU0NSQVBFIEZPUiBNT1JFIExJTktTIHwnIGluIG5hbWU6IG5hbWUgPSBuYW1lLnJlcGxhY2UoJ1NDUkFQRSBGT1IgTU9SRSBMSU5LUyB8JywnJykucmVwbGFjZSgnW0NPTE9SIGJsdWVdJywnJykucmVwbGFjZSgnWy9DT0xPUl0nLCcnKS5yZXBsYWNlKCdbQ09MT1IgeWVsbG93XScsJycpLnN0cmlwKCkNCglpZiBub3QgZGVzY3JpcHRpb246IGRlc2NyaXB0aW9uID0gJ0Fwb2NhbHlwc2UgNzIwJw0KCWRpYWxvZyA9IHhibWNndWkuRGlhbG9nKCkNCgl0eXBlID0gJ01PVklFJw0KCWRhdGUgPSBuYW1lDQoJdGhyZWFkcyA9IFtdDQoJaiA9IDANCgl0b3RhbHNjcmFwZXJzID0gMA0KCXVybCA9IHVybC5yZXBsYWNlKCdbQ09MT1IgYmx1ZV0nLCcnKS5yZXBsYWNlKCdbL0NPTE9SXScsJycpLnJlcGxhY2UoJ1tDT0xPUiBkZWVwc2t5Ymx1ZV0nLCcnKS5yZXBsYWNlKCdbQ09MT1IgeWVsbG93XScsJycpDQoJZGF0ZSA9IGRhdGUucmVwbGFjZSgnW0NPTE9SIGJsdWVdJywnJykucmVwbGFjZSgnWy9DT0xPUl0nLCcnKS5yZXBsYWNlKCdbQ09MT1IgZGVlcHNreWJsdWVdJywnJykucmVwbGFjZSgnfCcsJycpLnN0cmlwKCkNCglkYXRlID0gZGF0ZS5yZXBsYWNlKHVybCwnJykNCgluYW1lID0gcmUuc3ViKHInKFteXHNcd118XykrJywgJycsIG5hbWUpDQoJbmFtZSA9IHJlLnN1YihyJyArJywgJyAnLCBuYW1lKQ0KCVNlYXJjaCA9IHVybA0KCWdsb2JhbCBmaW5hbHNvdXJjZXMNCglmaW5hbHNvdXJjZXMgPSBbXQ0KCXRocmVhZHMgPSBbXQ0KCWogPSAwDQoJdG90YWxzY3JhcGVycyA9IDANCglmcm9tIHNjcmFwZXJzIGltcG9ydCBzb3VyY2VzDQoJX3NvdXJjZXMgPSBzb3VyY2VzKCkNCglmb3IgaW5kZXhlciBpbiBfc291cmNlczoNCgkJaWYgJ2FwcG9jJyBpbiBpbmRleGVyIG9yICdhaW8nIGluIGluZGV4ZXI6IGNvbnRpbnVlDQoJCXRocmVhZHMuYXBwZW5kKHdvcmtlcnMuVGhyZWFkKHJ1blNvdXJjZSwgaW5kZXhlclsxXSwgdHlwZSwgU2VhcmNoLCBkYXRlKSkNCglkcC5jcmVhdGUgKEFkZG9uVGl0bGUsIltCXVtDT0xPUiBibHVlXVNlYXJjaGluZyBGb3IgW0NPTE9SIHdoaXRlXSVzWy9CXVsvQ09MT1JdIiAlIFNlYXJjaC50aXRsZSgpKQ0KCXRpbWUuc2xlZXAoMS41KQ0KCVtpLnN0YXJ0KCkgZm9yIGkgaW4gdGhyZWFkc10NCglmb3IgbiBpbiByYW5nZSgwLCA0NSk6DQoJCWlmIGRwLmlzY2FuY2VsZWQoKTogYnJlYWsNCgkJYWxpdmUgPSBbeC5pc19hbGl2ZSgpIGZvciB4IGluIHRocmVhZHMgaWYgeC5pc19hbGl2ZSgpID09IFRydWVdDQoJCWRwLnVwZGF0ZShpbnQoKDEwMCAvIGZsb2F0KGxlbih0aHJlYWRzKSkpICogbGVuKFt4IGZvciB4IGluIHRocmVhZHMgaWYgeC5pc19hbGl2ZSgpID09IEZhbHNlXSkpLCAnRWxhcHNlZDogJXMnICUgKG4pLCAnUmVtYWluaW5nIFNjcmFwZXJzOiAlcycgJSBsZW4oYWxpdmUpLCAnTGlua3MgRm91bmQ6ICVzJyAlIGxlbihmaW5hbHNvdXJjZXMpKQ0KCQlpZiBsZW4oYWxpdmUpID09IDA6DQoJCQl0aW1lLnNsZWVwKDIpDQoJCQlicmVhaw0KCQl0aW1lLnNsZWVwKDEpDQoJZHAuY2xvc2UoKQ0KCXN0cmVhbXVybCA9IFtdIDsgc3RyZWFtbmFtZSA9IFtdDQoJX2ZpbmFsc291cmNlcyA9IHNvcnRlZChmaW5hbHNvdXJjZXMsIGtleT1sYW1iZGEgazoga1sncXVhbGl0eSddKQ0KCWZvciBpIGluIF9maW5hbHNvdXJjZXM6DQoJCWlmICdUb3JyZW50JyBpbiBpWyd0aXRsZSddOiAoaVsndGl0bGUnXSkgPSAnW0NPTE9SIHllbGxvd10nICsgKGlbJ3RpdGxlJ10pICsgJ1svQ09MT1JdJw0KCQllbGlmICdMaW5rU25hcHB5JyBpbiBpWyd0aXRsZSddOiAoaVsndGl0bGUnXSkgPSAnW0NPTE9SIGFxdWFdJyArIChpWyd0aXRsZSddKSArICdbL0NPTE9SXScNCgkJZWxpZiAnUkQnIGluIGlbJ3RpdGxlJ106IChpWyd0aXRsZSddKSA9ICdbQ09MT1IgYXF1YV0nICsgKGlbJ3RpdGxlJ10pICsgJ1svQ09MT1JdJw0KCQllbHNlOiAoaVsndGl0bGUnXSkgPSAnW0NPTE9SIHdoaXRlXScgKyAoaVsndGl0bGUnXSkgKyAnWy9DT0xPUl0nDQoJCXN0cmVhbXVybC5hcHBlbmQoaVsndXJsJ10pDQoJCXN0cmVhbW5hbWUuYXBwZW5kKGlbJ3RpdGxlJ10pDQoJY29tYmluZWQgPSBsaXN0KHppcChzdHJlYW11cmwsc3RyZWFtbmFtZSkpDQoJZm9yIHVybCx0aXRsZSBpbiBjb21iaW5lZDoNCgkJdGl0bGUgPSB0aXRsZS5lbmNvZGUoJ3V0Zi04JykNCgkJdXJsID0gdXJsLmVuY29kZSgndXRmLTgnKQ0KCQlkZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uLmVuY29kZSgndXRmLTgnKQ0KCQlpY29uaW1hZ2UgPSBpY29uaW1hZ2UuZW5jb2RlKCd1dGYtOCcpDQoJCWZhbmFydCA9IGZhbmFydC5lbmNvZGUoJ3V0Zi04JykNCgkJYWRkTGluaygiW0NPTE9SIGJsdWVdW0JdIiArIHRpdGxlICsgIlsvQl1bL0NPTE9SXSIsdXJsLDEwMDAsaWNvbmltYWdlLGZhbmFydCxkZXNjcmlwdGlvbikNCg0KZGVmIHJ1blNvdXJjZShjYWxsLCB0eXBlLCBuYW1lLHllYXIsSU1EQk5PPScnLHRvcnJlbnRzPScnKToNCglnZXRfc291cmNlcyA9IFtdDQoJZ2V0X3NvdXJjZXMgPSBjYWxsLkluZGV4KHR5cGUsIG5hbWUsIHllYXIsIElNREJOTywgdG9ycmVudHMpDQoJZmluYWxzb3VyY2VzLmV4dGVuZChnZXRfc291cmNlcykNCg0KZGVmIEdldE1lbnUoKToNCg0KCXVybCA9IGJhc2V1cmwNCgl1cmwyPXVybA0KCXBvcHVwKCkNCglnZXR0aW1lID0gaW50KGRhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCclSCVNJykpDQoJaWYgKGdldHRpbWUgPj0gMDAwMCkgYW5kIChnZXR0aW1lIDw9IDExNTkpOiBhID0gIk1vcm5pbmciDQoJZWxpZiAoZ2V0dGltZSA+PSAxMjAwKSBhbmQgKGdldHRpbWUgPD0gMTc1OSk6IGEgPSAiQWZ0ZXJub29uIg0KCWVsc2U6IGEgPSAiRXZlbmluZyINCglhZGRTdGFuZGFyZExpbmsoJ1tDT0xPUiB5ZWxsb3ddR29vZFtDT0xPUiBhcXVhXSAnICsgc3RyKGEpICsgJ1tDT0xPUiB5ZWxsb3ddIEZyb20gVGhlIEFwb2NhbHlwc2UgVGVhbVsvQ09MT1JdJywndXJsJywnMTInLGljb24sZmFuYXJ0cykNCglhZGRTdGFuZGFyZExpbmsoIltDT0xPUiB5ZWxsb3ddLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tWy9DT0xPUl0iLCd1cmwyJyw5OTksaWNvbixmYW5hcnRzKQ0KCWFkZERpcigiW0NPTE9SIHJlZF1bQl1TZWFyY2ggQWRkb25bL0JdWy9DT0xPUl0iLCdTJywyMCxTaWNvbixmYW5hcnRzKQ0KCWFkZERpcigiW0NPTE9SIGJsdWVdW0JdVE1EQiBUb3AgTW92aWVzWy9CXVsvQ09MT1JdIiwnaHR0cHM6Ly9hcGkudGhlbW92aWVkYi5vcmcvMy9tb3ZpZS9wb3B1bGFyP2FwaV9rZXk9JyArIHRtZGJhcGkgKyAnJmxhbmd1YWdlPWVuLVVTJnBhZ2U9MScsOCxpY29uLGZhbmFydHMpDQoJYWRkRGlyKCJbQ09MT1IgYmx1ZV1bQl1UTURCIENpbmVtYSBNb3ZpZXNbL0JdWy9DT0xPUl0iLCdodHRwczovL2FwaS50aGVtb3ZpZWRiLm9yZy8zL2Rpc2NvdmVyL21vdmllP2FwaV9rZXk9JyArIHRtZGJhcGkgKyAnJndpdGhfcmVsZWFzZV90eXBlPTJ8MyZyZWdpb249VVMnLDgsaWNvbixmYW5hcnRzKQ0KCWxpbms9T3BlbkxpbmsoYmFzZXVybCkNCgltYXRjaD0gcmUuZmluZGFsbCgnPGl0ZW0+KC4rPyk8L2l0ZW0+JyxsaW5rLGZsYWdzPXJlLkRPVEFMTCkNCglmb3IgaXRlbSBpbiBtYXRjaDoNCgkJdHJ5Og0KCQkJaWYgJzxtM3U+JyBpbiBpdGVtOg0KCQkJCW5hbWU9cmUuZmluZGFsbCgnPHRpdGxlPiguKz8pPC90aXRsZT4nLGl0ZW0sZmxhZ3M9cmUuRE9UQUxMKVswXQ0KCQkJCWljb25pbWFnZT1yZS5maW5kYWxsKCc8dGh1bWJuYWlsPiguKz8pPC90aHVtYm5haWw+JyxpdGVtLGZsYWdzPXJlLkRPVEFMTClbMF0NCgkJCQlmYW5hcnQ9cmUuZmluZGFsbCgnPGZhbmFydD4oLis/KTwvZmFuYXJ0PicsaXRlbSxmbGFncz1yZS5ET1RBTEwpWzBdDQoJCQkJdXJsPXJlLmZpbmRhbGwoJzxtM3U+KC4rPyk8L20zdT4nLGl0ZW0sZmxhZ3M9cmUuRE9UQUxMKVswXQ0KCQkJCWFkZERpcihuYW1lLHVybCwxMSxpY29uaW1hZ2UsZmFuYXJ0KQ0KCQkJZWxpZiAnPDI0Nz4n'
love = 'VTyhVTy0MJ06QDbWPDxWozSgMG1lMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWnJAiozygLJqyCKWyYzMcozEuoTjbWmk0nUIgLz5unJj+XP4eClx8Y3EbqJ1vozScoQ4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXIfjKD0XPDxWPJMuozSlqQ1lMF5znJ5xLJkfXPp8MzShLKW0CvthXm8cCP9zLJ5upaD+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDy1pzj9pzHhMzyhMTSfoPtaCQV0Am4bYvf/XGjiZwD3CvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWLJExETylXT5uoJHfqKWfYQLfnJAiozygLJqyYTMuozSlqPxAPtxWPJIfnJLtWmkzo2kxMKV+W2yhVTy0MJ06QDbWPDxWMTS0LG1lMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCv4eC2MioTEypw4bYvf/XGjiMz9fMTIlCv4eC3EbqJ1vozScoQ4bYvf/XGjiqTu1oJWhLJyfCv4eC2MuozSlqQ4bYvf/XGjiMzShLKW0CvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcQDbWPDxWMz9lVT5uoJHfqKWfYTywo25coJSaMFkzLJ5upaDtnJ4tMTS0LGbAPtxWPDxWLJExETylXT5uoJHfqKWfYQRfnJAiozygLJqyYTMuozSlqPxAPtxWPJIfp2H6QDbWPDxWoTyhn3Z9pzHhMzyhMTSfoPtaCTkcozf+XP4eClx8Y2kcozf+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPxAPtxWPDycMvOfMJ4boTyhn3ZcCG0kBt0XPDxWPDyxLKEuCKWyYzMcozEuoTjbWmk0nKEfMG4bYvf/XGjiqTy0oTH+Yvf/oTyhnm4bYvf/XGjioTyhnm4hXm90nUIgLz5unJj+XP4eClx8Y3EbqJ1vozScoQ4hXm9zLJ5upaD+XP4eClx8Y2MuozSlqQ4aXF5znJ5xLJkfXTy0MJ0cQDbWPDxWPJkwo3IhqQ1fMJ4boJS0L2tcQDbWPDxWPJMipvOhLJ1yYUIloPkcL29hnJ1uM2HfMzShLKW0VTyhVTEuqTR6QDbWPDxWPDyuMTEZnJ5eXT5uoJHfqKWfYQRjZQNfnJAiozygLJqyYTMuozSlqPxAPtxWPDyyoTyzVTkyovufnJ5eplx+ZGbAPtxWPDxWozSgMG1lMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPJywo25coJSaMG1lMF5znJ5xLJkfXPp8qTu1oJWhLJyfCvthXm8cCP90nUIgLz5unJj+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWMzShLKW0CKWyYzMcozEuoTjbWmkzLJ5upaD+XP4eClx8Y2MuozSlqQ4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXIfjKD0XPDxWPDyuMTEZnJ5eXT5uoJHfqKWfZvjmYTywo25coJSaMFkzLJ5upaDcQDbWPJI4L2IjqQcjLKAmQDbAPty4Lz1wYzI4MJA1qTIvqJyfqTyhXPqQo250LJyhMKVhH2I0Izyyq01iMTHbAGHcWlxAPt0XMTIzVRqyqRAioaEyoaDbozSgMFk1pzjfnJAiozygLJqyYTMuozSlqPx6QDbWMTyuoT9aVQ0trTWgL2q1nF5RnJSfo2pbXD0XPKIloQZ9qKWfQDbWoTyhnm1CpTIhGTyhnlu1pzjcQDbWoJS0L2t9VUWyYzMcozEuoTjbWmkcqTIgCvthXm8cCP9cqTIgCvpfoTyhnlkzoTSapm1lMF5RG1EOGRjcQDbWMz9lVTy0MJ0tnJ4toJS0L2t6QDbWPKElrGbAPtxWPJyzVPp8nJ1uM2H+WlOcovOcqTIgBt0XPDxWPDyhLJ1yCKWyYzMcozEuoTjbWmk0nKEfMG4bYvf/XGjiqTy0oTH+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWnJAiozygLJqyCKWyYzMcozEuoTjbWmk0nUIgLz5unJj+XP4eClx8Y3EbqJ1vozScoQ4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXIfjKFNtVPNtVPNtVPNtVN0XPDxWPDyzLJ5upaD9pzHhMzyhMTSfoPtaCTMuozSlqQ4bYvf/XGjiMzShLKW0CvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPKIloQ1lMF5znJ5xLJkfXPp8nJ1uM2H+XP4eClx8Y2ygLJqyCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPJSxMREcpvuhLJ1yYUIloPj5YTywo25coJSaMFkzLJ5upaDcQDbWPDyyoTyzVPp8rJ91qUIvMG4aVTyhVTy0MJ06QDbWPDxWPJ5uoJH9pzHhMzyhMTSfoPtaCUEcqTkyCvthXm8cCP90nKEfMG4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXIfjKD0XPDxWPDycL29hnJ1uM2H9pzHhMzyhMTSfoPtaCUEbqJ1vozScoQ4bYvf/XGjiqTu1oJWhLJyfCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqVPNtVPNtVPNtVPNtQDbWPDxWPJMuozSlqQ1lMF5znJ5xLJkfXPp8MzShLKW0CvthXm8cCP9zLJ5upaD+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWqKWfCKWyYzMcozEuoTjbWmk5o3I0qJWyCvthXm8cCP95o3I0qJWyCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPJSxMREcpvuhLJ1yYUIloPj1YTywo25coJSaMFkzLJ5upaDcQDbWPDyyoTyzVPp8Mz9fMTIlCvqcovOcqTIgBt0XPDxWPJEuqTR9pzHhMzyhMTSfoPtaCUEcqTkyCvthXm8cCP90nKEfMG4hXm9zo2kxMKV+XP4eClx8Y2MioTEypw4hXm90nUIgLz5unJj+XP4eClx8Y3EbqJ1vozScoQ4hXm9zLJ5upaD+XP4eClx8Y2MuozSlqQ4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXD0XPDxWPJMipvOhLJ1yYUIloPkcL29hnJ1uM2HfMzShLKW0VTyhVTEuqTR6QDbWPDxWPDyuMTERnKVbozSgMFk1pzjfZFkcL29hnJ1uM2HfMzShLKW0XD0XPDxWMJkmMGbAPtxWPDyfnJ5epm1lMF5znJ5xLJkfXPp8oTyhnm4bYvf/XGjioTyhnm4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXD0XPDxWPJyzVTkyovufnJ5eplx9CGR6QDbWPDxWPJEuqTR9pzHhMzyhMTSfoPtaCUEcqTkyCvthXm8cCP90nKEfMG4hXm9fnJ5eCvthXm8cCP9fnJ5eCv4eC3EbqJ1vozScoQ4bYvf/XGjiqTu1oJWhLJyfCv4eC2MuozSlqQ4bYvf/XGjiMzShLKW0CvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcQDbWPDxWPJkwo3IhqQ1fMJ4boJS0L2tcQDbWPDxWPJMipvOhLJ1yYUIloPkcL29hnJ1uM2HfMzShLKW0VTyhVTEuqTR6QDbWPDxWPDyuMTEZnJ5eXT5uoJHfqKWfYQRjZQNfnJAiozygLJqyYTMuozSlqPxAPtxWPDyyoTyzVTkyovufnJ5eplx+ZGbAPtxWPDxWozSgMG1lMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCvpfnKEyoFkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPJywo25coJSaMG1lMF5znJ5xLJkfXPp8qTu1oJWhLJyfCvthXm8cCP90nUIgLz5unJj+WlkcqTIgYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWMzShLKW0CKWyYzMcozEuoTjbWmkzLJ5upaD+XP4eClx8Y2MuozSlqQ4aYTy0MJ0fMzkuM3Z9pzHhER9HDHkZXIfjKD0XPDxWPDyuMTERnKVbozSgMFk1pzjmYQZfnJAiozygLJqyYTMuozSlqPxAPtxWMKuwMKO0BaOup3ZAPt0XPKuvoJZhMKuyL3I0MJW1nJk0nJ4bW0AioaEunJ5ypv5GMKEJnJI3GJ9xMFt1AFxaXD0XMTIzVSEAERWGD1WOHRHbqKWfXGbAPtyxLKEuVQ0tpzIkqJImqUZhM2I0XUIloPxhnaAiovtcQDbWqUW5Bt0XPDygo3McMKZtCFOxLKEuJlqlMKA1oUEmW10APtyyrTAypUD6QDbWPJEcLJkiMl5ho3EcMzywLKEco24bDJExo25HnKEfMFjtW1gQG0kCHvO5MJkfo3qqEJ5xVR9zVSWyp3IfqUZfVR9lVSEAERVtGz90VSWyp3OiozEcozqoY0ACGR9FKFpfVRSxMT9hnJAiovjtAGNjZPxAPtxWpKIcqPtcQDbWMz9lVTyhMz8tnJ4toJ92nJImBt0XPDxwqUW5Bt0XPDxWnJ1apTS0nPN9VPqbqUEjpmbiY2ygLJqyYaEgMTVho3WaY3DipP9ipzyanJ5uoPpAPtxWPKElrGbtqTy0oTHtCFOcozMiJlq0nKEfMFqqYzIhL29xMFtaqKEzYGtaXD0XPDxWMKuwMKO0VRgyrHIlpz9lBvO0nKEfMFN9VTyhMz9oW25uoJHaKF5yozAiMTHbW3I0Mv04WlxAPtxWPJywo24tCFOcozMiJlqjo3A0MKWspTS0nPqqQDbWPDygo3McMJyxVQ0tnJ5zo1fanJDaKD0XPDxWnJLtoz90VTywo246VTywo24tCFOOMTEiozywo24APtxWPJIfp2H6VTywo24tCFOcoJqjLKEbVPftnJAiot0XPDxWMzShLKW0VQ0tnJ5zo1faLzSwn2Elo3OspTS0nPqqQDbWPDycMvOho3DtMzShLKW0BvOzLJ5upaDtCFOzLJ5upaEmQDbWPDyyoUAyBvOzLJ5upaDtCFOcoJqjLKEbVPftMzShLKW0QDbWPDy0MKu0VQ0tnJ5zo1fao3MypaMcMKpaKF5yozAiMTHbW3I0Mv04WlxAPtxWPKElrGbtMTS0MFN9VTyhMz9oW3WyoTIup2IsMTS0MFqqVQftMTS0MFN9VTEuqTHhp3OfnKDbWl0aXIfjKD0XPDxWMKuwMKO0VRgyrHIlpz9lBvOxLKEyVQ0aWj0XPDxWoJ92nJIcMPN9VUA0pvugo3McMJyxXD0XPDxWqTy0oTHtCFOmqUWcpS9ho25sLKAwnJxbqTy0oTHcVQftqTI4qPN9VUA0pzyjK25ioy9up2AcnFu0MKu0XD0XPDxWLJExETylXPWoD09ZG1VtMTIypUAerJWfqJIqVvNeVTEuqTHtXlNaVUjtJ0ACGR9FVTWfqJIqWlNeVUEcqTkyVPftVyfiD09ZG1WqVvk0nKEfMFj5YTywo24fMzShLKW0YUEyrUDcQDbWPFAyrTAypUDtBvOjLKAmQDbWqUW5Bt0XPDyhMKu0pTSaMFN9VUIloP5mpTkcqPtapTSaMG0aXIfgZI0APtxWL3IlpzIhqUOuM2HtCFO1pzjhp3OfnKDbW3OuM2H9WlyoZS0APtxWozI4qUOuM2IhqJ1vMKVtCFOcoaDbozI4qUOuM2HcVPftZD0XPDyhMKu0pTSaMKIloPN9VTA1paWyoaEjLJqyXlqjLJqyCFpep3ElXT5yrUEjLJqyoaIgLzIlXD0XPDyuMTERnKVbVygQG0kCHvOlMJEqJ0WqGzI4qPODLJqyJl9PKIfiD09ZG1WqVvkhMKu0pTSaMKIloPj4YRSxMT9hnJAiovkzLJ5upaDfW0qyqPOAo3WyVSWyp3IfqUZaXD0XPJI4L2IjqQbtpTSmpj0XMTIzVUA0pzyjK25ioy9up2AcnFumqUWcozpcBt0XVPNtVPpaWlOFMKE1pz5mVUEbMFOmqUWcozptq2y0nT91qPOho24tDIAQFHxtL2uupzSwqTIlplpaWj0XVPNtVUA0pzyjpTIxVQ0tXTZtMz9lVTZtnJ4tp3ElnJ5aVTyzVQNtCPOipzDbLlxtCPNkZwpcQDbtVPNtpzI0qKWhVPpaYzcinJ4bp3ElnKOjMJDcQDcxMJLtH2IupzAbXPx6QDbWMz91ozDtCFNjQDbWp3ElnJ5aVQ0aWj0XPJgyrJWiLKWxVQ0trTWgLl5YMKyvo2SlMPumqUWcozpfVPqoD09ZG1VtrJIfoT93KIgPKIqbLKDtDKWyVSqyVRkio2gcozptEz9lVQ8tJl9PKIfiD09ZG1WqWlxAPtyeMKyvo2SlMP5xo01iMTSfXPxAPtycMvOeMKyvo2SlMP5cp0AiozMcpz1yMPtcBt0XPDymqUWcozptCFOeMKyvo2SlMP5aMKEHMKu0XPxAPtxWnJLtoTIhXUA0pzyhMlx+ZGbAPtxWPKEypz0tCFOmqUWcozphoT93MKVbXD0XPDyyoUAyBt0XPDxWMTyuoT9aYz5iqTyznJAuqTyiovuOMTEioyEcqTkyYPNaJ0ACGR9FVUyyoTkiq11DoTIup2HtEJ50MKVtDFOGMJSlL2ttITIloIfiD09ZG1WqWljtDJExo25cL29hYPNlAGNjXD0XPDxWpKIcqPtcQDbWMJkmMGbAPtxWMTyuoT9aYz5iqTyznJAuqTyiovuOMTEioyEcqTkyYPNaJ0ACGR9FVUyyoTkiq11GMJSlL2ttEzIuqUIlMFOTLJyfMJDfVSWypT9lqPOHolORMKMoY0ACGR9FKFpfVRSxMT9hnJAiovjtZwHjZPxAPtxWpKIcqPtcQDbWp3EupaDtCFOlMKS1MKA0pl5aMKDbLzSmMKIloPxhL29hqTIhqN0XPJEcpaZtCFOlMF5znJ5xLJkfXPp8Mz9fMTIlCvthXw8cCP9zo2kxMKV+WlkmqTSlqPkzoTSapm1lMF5RG1EOGRjcQDbWMz9lVTEcpvOcovOxnKWmBt0XPDy0pax6QDbWPDyxo21unJ4tCFOlMKS1MKA0pl5aMKDbMTylXF5wo250MJ50QDbWPDygLKEwnPN9VUWyYzMcozEuoTjbWmkcqTIgCvthXw8cCP9cqTIgCvpfMT9gLJyhYTMfLJqmCKWyYxECIRSZGPxAPtxWPJMipvOwo250MJ50VTyhVT1uqTAbBt0XPDxWPKEcqTkyMzyhMPN9VUWyYzMcozEuoTjbWmk0nKEfMG4bYvb/XGjiqTy0oTH+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDycMvO0MKWgVQ09VUEcqTkyMzyhMP5fo3qypvtcBt0XPDxWPDyzo3IhMPNeCFNkQDbWPDxWPJygLJqyVQ0tpzHhMzyhMTSfoPtaCUEbqJ1vozScoQ4bYvb/XGjiqTu1oJWhLJyfCvpfL29hqTIhqPkzoTSapm1lMF5RG1EOGRjcQDbWPDxWPJMuozSlqPN9VUWyYzMcozEuoTjbWmkzLJ5upaD+XP4dClx8Y2MuozSlqQ4aYTAioaEyoaDfMzkuM3Z9pzHhER9HDHkZXD0XPDxWPDyfnJ5eplN9VUWyYzMcozEuoTjbWmkfnJ5eCvthXw8cCP9fnJ5eCvpfL29hqTIhqPkzoTSapm1lMF5RG1EOGRjcQDbWPDxWPJyzVTkyovufnJ5eplxtCG0kBt0XPDxWPDxWMTS0LFN9VUWyYzMcozEuoTjbWmk0nKEfMG4bYvf/XGjiqTy0oTH+Yvf/oTyhnm4bYvf/XGjioTyhnm4hXm90nUIgLz5unJj+XP4eClx8Y3EbqJ1vozScoQ4hXm9zLJ5upaD+XP4eClx8Y2MuozSlqQ4aYTAioaEyoaDfMzkuM3Z9pzHhER9HDHkZXD0XPDxWPDxWMz9lVUEcqTkyYTkcozffnJ1uM2HfMzShLKW0VTyhVTEuqTR6QDbWPDxWPDxWLJExGTyhnlu0nKEfMJMcozDfoTyhnljkZQNjYTygLJqyYTMuozSlqPxAPtxWPDxWMJkcMvOfMJ4boTyhn3ZcCwR6QDbWPDxWPDyhLJ1yCKWyYzMcozEuoTjbWmk0nKEfMG4bYvf/XGjiqTy0oTH+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWPJywo25coJSaMG1lMF5znJ5xLJkfXPp8qTu1oJWhLJyfCvthXm8cCP90nUIgLz5unJj+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWPJMuozSlqQ1lMF5znJ5xLJkfXPp8MzShLKW0CvthXm8cCP9zLJ5upaD+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPDxWPJSxMRkcozfbozSgMFkxnKVfZlkcL29hnJ1uM2HfMzShLKW0XD0XPDxWPJIfnJLtqTIloFOcovO0nKEfMJMcozDhoT93MKVbXGbAPtxWPDxWMz91ozDtXm0tZD0XPDxWPDycoJSaMFN9VUWyYzMcozEuoTjbWmk0nUIgLz5unJj+XP4dClx8Y3EbqJ1vozScoQ4aYTAioaEyoaDfMzkuM3Z9pzHhER9HDHkZXD0XPDxWPDyzLJ5upaDtCFOlMF5znJ5xLJkfXPp8MzShLKW0CvthXw8cCP9zLJ5upaD+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPxAPtxWPDxWoTyhn3ZtCFOlMF5znJ5xLJkfXPp8oTyhnm4bYvb/XGjioTyhnm4aYTAioaEyoaDfMzkuM3Z9pzHhER9HDHkZXD0XPDxWPDycMvOfMJ4boTyhn3ZcVQ09ZGbAPtxWPDxWPJEuqTRtCFOlMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCv4eC2kcozf+XP4eClx8Y2kcozf+Yvf/qTu1oJWhLJyfCvthXm8cCP90nUIgLz5unJj+Yvf/MzShLKW0CvthXm8cCP9zLJ5upaD+Wlkwo250MJ50YTMfLJqmCKWyYxECIRSZGPxAPtxWPDxWPJMipvO0nKEfMFkfnJ5eYTygLJqyYTMuozSlqPOcovOxLKEuBt0XPDxWPDxWPJSxMRkcozfbqTy0oTIznJ5xYTkcozffZGNjZPkcoJSaMFkzLJ5upaDcQDbWPDxWPJIfnJLtoTIhXTkcozgmXG4kBt0XPDxWPDxWozSgMG1lMF5znJ5xLJkfXPp8qTy0oTH+XP4eClx8Y3EcqTkyCvpfL29hqTIhqPkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPDycL29hnJ1uM2H9pzHhMzyhMTSfoPtaCUEbqJ1vozScoQ4bYvf/XGjiqTu1oJWhLJyfCvpfL29hqTIhqPkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPDyzLJ5upaD9pzHhMzyhMTSfoPtaCTMuozSlqQ4bYvf/XGjiMzShLKW0CvpfL29hqTIhqPkzoTSapm1lMF5RG1EOGRjcJmOqQDbWPDxWPDyuMTEZnJ5eXT5uoJHfMTylYQZfnJAiozygLJqyYTMuozSlqPxAPtxWPDyyoUAyBvOwo250nJ51MD0XPDyyrTAypUD6VUOup3ZAPtycMvOzo3IhMPN9CFNjBt0XPDywnT9cL2HtCFO4Lz1wM3IcYxEcLJkiMltcYayyp25iXRSxMT9hITy0oTHfVPqoD09ZG1VtrJIfoT93'
god = 'XUZpbG0gW0NPTE9SIGJsdWVdJXNbQ09MT1IgeWVsbG93XSBOb3QgSW4gQXBvY2FseXBzZSwgU2hhbGwgV2UgU2NyYXBlIGxpbmtzIEluc3RlYWQ/Wy9DT0xPUl0nICV0ZXJtLnRpdGxlKCksJycseWVzbGFiZWw9J1llcyBQbGVhc2UnLG5vbGFiZWw9J05vIFRoYW5reW91JykNCgkJaWYgY2hvaWNlOiBUTURCU0NSQVBFKCdodHRwczovL2FwaS50aGVtb3ZpZWRiLm9yZy8zL3NlYXJjaC9tb3ZpZT9hcGlfa2V5PScgKyB0bWRiYXBpICsgJyZxdWVyeT0nICsgdGVybSkNCgkJZWxzZTogcXVpdCgpDQoNCmRlZiBUd2VudHk3KHVybCk6DQoJdXJsID0gJ2h0dHBzOi8vd3d3LmFyY29uYWl0di51cy9pbmRleC5waHAnDQoJdWEgPSAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcyLjAuMzYyNi4xMjEgU2FmYXJpLzUzNy4zNicNCgloZWFkZXJzID0geydVc2VyLUFnZW50JzogdWF9DQoJbGluayA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9aGVhZGVycykudGV4dA0KCXNvdXAgPSBCZWF1dGlmdWxTb3VwKGxpbmssICdodG1sNWxpYicpDQoJZGF0YSA9IHNvdXAuZmluZF9hbGwoJ2RpdicgLCBjbGFzc189eydjb2wteHMtNiBjb2wtbS00IGNvbC1sLTInfSkNCgliYXNlZG9tYWluID0gJ2h0dHBzOi8vd3d3LmFyY29uYWl0di51cy8nDQoJZm9yIGkgaW4gZGF0YToNCgkJdGl0bGUgPSBpLmltZ1snYWx0J10NCgkJZGVzY3JpcHRpb24gPSBpLmFbJ3RpdGxlJ10NCgkJdXJsID0gaS5hWydocmVmJ10NCgkJaW1hZ2UgPSBpLmltZ1snc3JjJ10NCgkJaWYgbm90IGJhc2Vkb21haW4gaW4gdXJsOiB1cmwgPSBiYXNlZG9tYWluK3VybA0KCQlpZiBub3QgYmFzZWRvbWFpbiBpbiBpbWFnZTogaW1hZ2UgPSBiYXNlZG9tYWluK2ltYWdlDQoJCWFkZExpbmsoIltDT0xPUiB5ZWxsb3ddW0JdIiArIHRpdGxlICsgIlsvQl1bL0NPTE9SXSIsdXJsLDcsaW1hZ2UsZmFuYXJ0LGRlc2NyaXB0aW9uKQ0KCQkNCmRlZiBSZXNvbHZlVHdlbnR5NyhuYW1lLHVybCxpY29uaW1hZ2UpOg0KDQoJdWEgPSAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcyLjAuMzYyNi4xMjEgU2FmYXJpLzUzNy4zNicNCgloZWFkZXJzID0geydVc2VyLUFnZW50JzogdWF9DQoJbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz1oZWFkZXJzKS5jb250ZW50DQoJcGF0dGVybiA9IHInJycoZXZhbFwoZnVuY3Rpb25cKHAsYSxjLGssZSwoPzpyfGQpLiopJycnDQoJZ2V0cGFja2VkID0gcmUuZmluZGFsbChwYXR0ZXJuLGxpbmspWzBdDQoJaW1wb3J0IGpzdW5wYWNrDQoJdW5wYWNrID0ganN1bnBhY2sudW5wYWNrKGdldHBhY2tlZCkNCglwbGF5YWJsZSA9IHJlLmZpbmRhbGwoJycnc3JjOlsnIl0oLio/KVsnIl0nJycsdW5wYWNrLGZsYWdzPXJlLkRPVEFMTClbMF0NCglwbGF5ID0gcGxheWFibGUrKCd8VXNlci1BZ2VudD0lcyZSZWZlcmVyPSVzJlgtQ3VzdG9tSGVhZGVyPXZpZGVvanMnICUgKHVhLHVybCkpDQoJUExBWUxJTksobmFtZSxwbGF5LGljb25pbWFnZSkNCg0KZGVmIFBpbigpOg0KCXBpbiA9IHNlbGZBZGRvbi5nZXRTZXR0aW5nKCdwaW4nKQ0KCWlmIHBpbiA9PSAnJzogcGluID0gJ0VYUElSRUQnDQoJaWYgcGluID09ICdFWFBJUkVEJzoNCgkJc2VsZkFkZG9uLnNldFNldHRpbmcoJ3BpbnVzZWQnLCdGYWxzZScpDQoJCWRpYWxvZy5vayhBZGRvblRpdGxlLCJbQ09MT1IgeWVsbG93XVBsZWFzZSB2aXNpdCBbQ09MT1IgbGltZV1odHRwczovL3BpbnN5c3RlbS5jby51a1tDT0xPUiB5ZWxsb3ddIHRvIGdlbmVyYXRlIGFuIEFjY2VzcyBUb2tlbiBGb3IgW0NPTE9SIGxpbWVdQXBvY2FseXBzZSA3MjBbQ09MT1IgeWVsbG93XSB0aGVuIGVudGVyIGl0IGFmdGVyIGNsaWNraW5nIG9rWy9DT0xPUl0iKQ0KCQlzdHJpbmcgPScnDQoJCWtleWJvYXJkID0geGJtYy5LZXlib2FyZChzdHJpbmcsICdbQ09MT1IgcmVkXVBsZWFzZSBFbnRlciBQaW4gR2VuZXJhdGVkIEZyb20gV2Vic2l0ZShDYXNlIFNlbnNpdGl2ZSlbL0NPTE9SXScpDQoJCWtleWJvYXJkLmRvTW9kYWwoKQ0KCQlpZiBrZXlib2FyZC5pc0NvbmZpcm1lZCgpOg0KCQkJc3RyaW5nID0ga2V5Ym9hcmQuZ2V0VGV4dCgpDQoJCQlpZiBsZW4oc3RyaW5nKT4xOg0KCQkJCXRlcm0gPSBzdHJpbmcudGl0bGUoKQ0KCQkJCXNlbGZBZGRvbi5zZXRTZXR0aW5nKCdwaW4nLHRlcm0pDQoJCQkJUGluKCkNCgkJCWVsc2U6IHF1aXQoKQ0KCQllbHNlOg0KCQkJcXVpdCgpDQoJaWYgbm90ICdFWFBJUkVEJyBpbiBwaW46DQoJCXBpbnVybGNoZWNrID0gKCdodHRwczovL3BpbnN5c3RlbS5jby51ay9zZXJ2aWNlLnBocD9jb2RlPSVzJnBsdWdpbj1SblZqYTFsdmRTRScgJSBwaW4pDQoJCWxpbmsgPSByZXF1ZXN0cy5nZXQocGludXJsY2hlY2spLmNvbnRlbnQNCgkJaWYgbGVuKGxpbmspIDw9MiBvciAnUGluIEV4cGlyZWQnIGluIGxpbms6DQoJCQlzZWxmQWRkb24uc2V0U2V0dGluZygncGluJywnRVhQSVJFRCcpDQoJCQlQaW4oKQ0KCQllbHNlOg0KCQkJcmVnaXN0ZXJwaW4gPSBzZWxmQWRkb24uZ2V0U2V0dGluZygncGludXNlZCcpDQoJCQlpZiByZWdpc3RlcnBpbiA9PSAnRmFsc2UnOg0KCQkJCXRyeToNCgkJCQkJcmVxdWVzdHMuZ2V0KCdodHRwczovL3BpbnN5c3RlbS5jby51ay9jaGVja2VyLnBocD9jb2RlPTk5OTk5JnBsdWdpbj1DaW5lbWEnKS5jb250ZW50DQoJCQkJCXNlbGZBZGRvbi5zZXRTZXR0aW5nKCdwaW51c2VkJywnVHJ1ZScpDQoJCQkJZXhjZXB0OiBwYXNzDQoJCQllbHNlOiBwYXNzDQoNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMjIFRIRSBTQ1JBUFBFUlMNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCg0KDQoNCg0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KIyMgVEhFIElNUE9SVEFOVCBTVFVGRg0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQpkZWYgQ0xFQU5VUCh0ZXh0KToNCg0KCXRleHQgPSBzdHIodGV4dCkNCgl0ZXh0ID0gdGV4dC5yZXBsYWNlKCdcXHInLCcnKQ0KCXRleHQgPSB0ZXh0LnJlcGxhY2UoJ1xcbicsJycpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnXFx0JywnJykNCgl0ZXh0ID0gdGV4dC5yZXBsYWNlKCdcXCcsJycpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnPGJyIC8+JywnXG4nKQ0KCXRleHQgPSB0ZXh0LnJlcGxhY2UoJzxociAvPicsJycpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnJiMwMzk7JywiJyIpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnJiMzOTsnLCInIikNCgl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmcXVvdDsnLCciJykNCgl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmcnNxdW87JywiJyIpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnJmFtcDsnLCImIikNCgl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmIzgyMTE7JywiJiIpDQoJdGV4dCA9IHRleHQucmVwbGFjZSgnJiM4MjE3OycsIiciKQ0KCXRleHQgPSB0ZXh0LnJlcGxhY2UoJyYjMDM4OycsIiYiKQ0KCXRleHQgPSB0ZXh0LnJlcGxhY2UoJyYjODIxMTsnLCItIikNCgl0ZXh0ID0gdGV4dC5sc3RyaXAoJyAnKQ0KCXRleHQgPSB0ZXh0LmxzdHJpcCgnCScpDQoNCglyZXR1cm4gdGV4dA0KDQpkZWYgUExBWUxJTksobmFtZSxsaW5rLGljb25pbWFnZSk6DQoJaWYgJ2xpbWV0b3JyZW50cycgaW4gbGluazoNCgkJdWEgPSAoJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV2luNjQ7IHg2NCkgJw0KCQkJCSdBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSAnDQoJCQkJJ0Nocm9tZS82NS4wLjMzMjUuMTgxIFNhZmFyaS81MzcuMzYnKQ0KCQlwbGF5YWJsZSA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9eyJVc2VyLUFnZW50Ijp1YX0pLmNvbnRlbnQNCgkJcGxheSA9IHJlLmZpbmRhbGwoJycnaHJlZj1bJyJdKG1hZ25ldDpcP3h0PXVybjouKj8pPScnJyxwbGF5YWJsZSxmbGFncz1yZS5ET1RBTEwpWzBdDQoJCWlmIHBsYXk6DQoJCQlobWYgPSByZXNvbHZldXJsLkhvc3RlZE1lZGlhRmlsZSh1cmw9cGxheSkNCgkJCWlmIGhtZi52YWxpZF91cmwoKTogbGluayA9IGhtZi5yZXNvbHZlKCkNCgkJCWRpYWxvZy5ub3RpZmljYXRpb24oQWRkb25UaXRsZSwgJ1tDT0xPUiB5ZWxsb3ddSHVudGluZyBMaW5rIE5vdyBCZSBQYXRpZW50Wy9DT0xPUl0nLCBBZGRvbmljb24sIDI1MDApDQoJCQl4Ym1jcGx1Z2luLnNldFJlc29sdmVkVXJsKGludChzeXMuYXJndlsxXSksIFRydWUsIHhibWNndWkuTGlzdEl0ZW0ocGF0aD1saW5rKSkNCgkJCXF1aXQoKQ0KCQllbHNlOiBkaWFsb2cubm90aWZpY2F0aW9uKEFkZG9uVGl0bGUsIltCXVtDT0xPUiB5ZWxsb3ddTGltZVRvcnJlbnQgRmFpbGVkIFRvIFBsYXlbL0JdWy9DT0xPUl0iICxpY29uLDUwMDApDQoJaWYgJ2FjZXN0cmVhbScgaW4gdXJsOg0KCQkJZGlhbG9nLm5vdGlmaWNhdGlvbihBZGRvblRpdGxlLCAnW0NPTE9SIHNreWJsdWVdUmVzb2x2ZSBBY2VzdHJlYW0gTGluayBOb3dbL0NPTE9SXScsIGljb24sIDUwMDApDQoJCQl1cmwxID0gInBsdWdpbjovL3Byb2dyYW0ucGxleHVzLz91cmw9IiArIHVybCArICImbW9kZT0xJm5hbWU9YWNlc3RyZWFtKyINCgkJCWxpeiA9IHhibWNndWkuTGlzdEl0ZW0obmFtZSxpY29uSW1hZ2U9aWNvbmltYWdlLCB0aHVtYm5haWxJbWFnZT1pY29uaW1hZ2UpDQoJCQlsaXouc2V0UGF0aCh1cmwpDQoJCQl4Ym1jLlBsYXllciAoKS5wbGF5KHVybDEsIGxpeiwgRmFsc2UpDQoJCQlxdWl0KCkNCgllbHNlOg0KCQl0cnk6DQoJCQlobWYgPSByZXNvbHZldXJsLkhvc3RlZE1lZGlhRmlsZSh1cmw9bGluaykNCgkJCWlmIGhtZi52YWxpZF91cmwoKTogbGluayA9IGhtZi5yZXNvbHZlKCkNCgkJCWRpYWxvZy5ub3RpZmljYXRpb24oQWRkb25UaXRsZSwgJ1tDT0xPUiB5ZWxsb3ddSHVudGluZyBMaW5rIE5vdyBCZSBQYXRpZW50Wy9DT0xPUl0nLCBBZGRvbmljb24sIDI1MDApDQoJCQl4Ym1jcGx1Z2luLnNldFJlc29sdmVkVXJsKGludChzeXMuYXJndlsxXSksIFRydWUsIHhibWNndWkuTGlzdEl0ZW0ocGF0aD1saW5rKSkNCgkJCXF1aXQoKQ0KCQlleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQoJCQlkaWFsb2cubm90aWZpY2F0aW9uKEFkZG9uVGl0bGUsIltCXVtDT0xPUiB5ZWxsb3ddJXNbL0JdWy9DT0xPUl0iICUgc3RyKGUpLGljb24sNTAwMCkNCgkJCXF1aXQoKQ0KDQpkZWYgYWRkRGlyKG5hbWUsdXJsLG1vZGUsaWNvbmltYWdlLGZhbmFydCxkZXNjcmlwdGlvbj0nJyk6DQoNCgl0cnk6IGRlc2NyaXB0aW9uID0gZGVzY3JpcHRpb24uZW5jb2RlKGVuY29kaW5nPSdVVEYtOCcsZXJyb3JzPSdzdHJpY3QnKQ0KCWV4Y2VwdCA6IHBhc3MNCgl1PXN5cy5hcmd2WzBdKyI/dXJsPSIrdXJsbGliLnF1b3RlX3BsdXModXJsKSsiJm1vZGU9IitzdHIobW9kZSkrIiZuYW1lPSIrdXJsbGliLnF1b3RlX3BsdXMobmFtZSkrIiZpY29uaW1hZ2U9Iit1cmxsaWIucXVvdGVfcGx1cyhpY29uaW1hZ2UpKyImZmFuYXJ0PSIrdXJsbGliLnF1b3RlX3BsdXMoZmFuYXJ0KSsiJmRlc2NyaXB0aW9uPSIrdXJsbGliLnF1b3RlX3BsdXMoZGVzY3JpcHRpb24pDQoJb2s9VHJ1ZQ0KCWxpej14Ym1jZ3VpLkxpc3RJdGVtKG5hbWUsIGljb25JbWFnZT1pY29uaW1hZ2UsIHRodW1ibmFpbEltYWdlPWljb25pbWFnZSwpDQoJbGl6LnNldFByb3BlcnR5KCAiZmFuYXJ0X0ltYWdlIiwgZmFuYXJ0ICkNCglsaXouc2V0UHJvcGVydHkoICJpY29uX0ltYWdlIiwgaWNvbmltYWdlICkNCglsaXouc2V0SW5mbygndmlkZW8nLCB7J1Bsb3QnOiBkZXNjcmlwdGlvbn0pDQoJdmlldz14Ym1jcGx1Z2luLnNldENvbnRlbnQoaW50KHN5cy5hcmd2WzFdKSwgJ21vdmllcycpDQoJb2s9eGJtY3BsdWdpbi5hZGREaXJlY3RvcnlJdGVtKGhhbmRsZT1pbnQoc3lzLmFyZ3ZbMV0pLHVybD11LGxpc3RpdGVtPWxpeixpc0ZvbGRlcj1UcnVlKQ0KCXJldHVybiBvaw0KDQpkZWYgYWRkTGluayhuYW1lLCB1cmwsIG1vZGUsIGljb25pbWFnZSwgZmFuYXJ0LCBkZXNjcmlwdGlvbj0nJyxmYW1pbHk9JycpOg0KDQoJdT1zeXMuYXJndlswXSsiP3VybD0iK3VybGxpYi5xdW90ZV9wbHVzKHVybCkrIiZtb2RlPSIrc3RyKG1vZGUpKyImbmFtZT0iK3VybGxpYi5xdW90ZV9wbHVzKG5hbWUpKyImaWNvbmltYWdlPSIrdXJsbGliLnF1b3RlX3BsdXMoaWNvbmltYWdlKSsiJmZhbmFydD0iK3VybGxpYi5xdW90ZV9wbHVzKGZhbmFydCkNCglvaz1UcnVlDQoJbGl6PXhibWNndWkuTGlzdEl0ZW0obmFtZSwgaWNvbkltYWdlPWljb25pbWFnZSwgdGh1bWJuYWlsSW1hZ2U9aWNvbmltYWdlKQ0KCWxpei5zZXRQcm9wZXJ0eSggImZhbmFydF9JbWFnZSIsIGZhbmFydCApDQoJbGl6LnNldFByb3BlcnR5KCAiaWNvbl9JbWFnZSIsIGljb25pbWFnZSApDQoJbGl6LnNldEluZm8oJ3ZpZGVvJywgeydQbG90JzogZGVzY3JpcHRpb259KQ0KCWxpei5zZXRQcm9wZXJ0eSgnSXNQbGF5YWJsZScsICd0cnVlJykNCgl2aWV3PXhibWNwbHVnaW4uc2V0Q29udGVudChpbnQoc3lzLmFyZ3ZbMV0pLCAnbW92aWVzJykNCglvaz14Ym1jcGx1Z2luLmFkZERpcmVjdG9yeUl0ZW0oaGFuZGxlPWludChzeXMuYXJndlsxXSksdXJsPXUsbGlzdGl0ZW09bGl6LGlzRm9sZGVyPUZhbHNlKQ0KCXJldHVybiBvaw0KDQpkZWYgYWRkU3RhbmRhcmRMaW5rKG5hbWUsIHVybCwgbW9kZSwgaWNvbmltYWdlLCBmYW5hcnQsIGRlc2NyaXB0aW9uPScnLGZhbWlseT0nJyk6DQoNCgl1PXN5cy5hcmd2WzBdKyI/dXJsPSIrdXJsbGliLnF1b3RlX3BsdXModXJsKSsiJm1vZGU9IitzdHIobW9kZSkrIiZuYW1lPSIrdXJsbGliLnF1b3RlX3BsdXMobmFtZSkrIiZpY29uaW1hZ2U9Iit1cmxsaWIucXVvdGVfcGx1cyhpY29uaW1hZ2UpKyImZmFuYXJ0PSIrdXJsbGliLnF1b3RlX3BsdXMoZmFuYXJ0KQ0KCW9rPVRydWUNCglsaXo9eGJtY2d1aS5MaXN0SXRlbShuYW1lLCBpY29uSW1hZ2U9aWNvbmltYWdlLCB0aHVtYm5haWxJbWFnZT1pY29uaW1hZ2UpDQoJbGl6LnNldFByb3BlcnR5KCAiZmFuYXJ0X0ltYWdlIiwgZmFuYXJ0ICkNCglsaXouc2V0UHJvcGVydHkoICJpY29uX0ltYWdlIiwgaWNvbmltYWdlICkNCglsaXouc2V0SW5mbygndmlkZW8nLCB7J1Bsb3QnOiBkZXNjcmlwdGlvbn0pDQoJb2s9eGJtY3BsdWdpbi5hZGREaXJlY3RvcnlJdGVtKGhhbmRsZT1pbnQoc3lzLmFyZ3ZbMV0pLHVybD11LGxpc3RpdGVtPWxpeixpc0ZvbGRlcj1GYWxzZSkNCglyZXR1cm4gb2sNCiAgICANCmRlZiBzaG93VGV4dChoZWFkaW5nLCB0ZXh0KToNCg0KICAg'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))