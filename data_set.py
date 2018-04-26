#!usr/bin/env python3

"""
turn indo function to iterate if possible :s
"""
ch = 8
filename = '5pkt.pcap'
end_bytes = 4

with open(filename, "rb") as f:

    cnt_bytes = header_size
    dataset_size = ch * 2 * 4
    while True:

        if not byte:
            break
        else:

            f.read(cnt_bytes) #run over headers
            data_set = f.read(dataset_size)
            cnt_bytes = header_size + end_bytes
"""
Infos:

The number of bytes on header & end are the same for at least
one file. It changes on only one condition, but it's not going
to happen here.
It's a constant pkt size, it can have zeros on sample place, 
but will be filled with something.

"""
