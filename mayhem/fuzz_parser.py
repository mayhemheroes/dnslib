#!/usr/bin/env python3
import atheris
import sys
import tempfile

with atheris.instrument_imports():
    import dnslib


@atheris.instrument_func
def TestOneInput(data):
    try:
        data = data.decode('utf-8', errors='ignore').encode('utf-8')
        dnslib.DNSRecord.parse(data)
    except dnslib.DNSError as e:
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()


