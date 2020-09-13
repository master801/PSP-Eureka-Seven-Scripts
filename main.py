#!/usr/bin/env python3

import os
import argparse
import glob
import struct
import io

import constants


def find_files(_dir):
    xpk_files = []
    for root, subdirs, files in os.walk(_dir):
        if len(files) < 1:  # Skip empty dirs
            continue
        for spk in glob.iglob(root + constants.FILE_PATH_SEPARATOR + '*.spk'):  # spk files
            xpk_files.append(spk)
            continue
        for dpk in glob.iglob(root + constants.FILE_PATH_SEPARATOR + '*.dpk'):  # dpk files
            xpk_files.append(dpk)
            continue
        continue
    return xpk_files


def read_entry(entry_data):
    offset_b = entry_data.read(0x04)
    len_b = entry_data.read(0x04)
    idk1_b = entry_data.read(0x04)
    idk2_b = entry_data.read(0x04)
    idk3_b = entry_data.read(0x04)
    idk4_b = entry_data.read(0x04)
    idk5_b = entry_data.read(0x04)
    idk6_b = entry_data.read(0x04)

    path_b = b''
    while True:
        cache = entry_data.read(1)
        if cache != b'\x00':
            path_b += cache
            pass
        else:
            break
        continue

    idk7_b = b'\x00' + entry_data.read(0x03)  # Include 0x00 and ONLY read 3 bytes, since 0x00 is used as a terminator
    idk8_b = entry_data.read(0x04)
    idk9_b = entry_data.read(0x04)
    idk10_b = entry_data.read(0x04)
    idk11_b = entry_data.read(0x04)
    idk12_b = entry_data.read(0x04)
    idk13_b = entry_data.read(0x04)
    idk14_b = entry_data.read(0x04)
    idk15_b = entry_data.read(0x04)
    idk16_b = entry_data.read(0x04)
    idk17_b = entry_data.read(0x04)

    path = path_b.decode(encoding='utf-8')

    return constants.Entry(
        offset=offset_b,
        len_=len_b,
        path=path,
        idk1=idk1_b,
        idk2=idk2_b,
        idk3=idk3_b,
        idk4=idk4_b,
        idk5=idk5_b,
        idk6=idk6_b,
        idk7=idk7_b,
        idk8=idk8_b,
        idk9=idk9_b,
        idk10=idk10_b,
        idk11=idk11_b,
        idk12=idk12_b,
        idk13=idk13_b,
        idk14=idk14_b,
        idk15=idk15_b,
        idk16=idk16_b,
        idk17=idk17_b,
    )


def read_xpk_files(xpk_files, output):
    for xpk_file in xpk_files:
        print('Reading file \"{}\"...'.format(xpk_file))
        xpk_io = open(xpk_file, 'rb+')

        # Check magic
        if xpk_io.read(len(constants.HEADER)) == constants.HEADER:
            print('Passed magic check')
            pass
        else:
            print('Failed magic check!')
            xpk_io.close()
            continue

        entries_b = xpk_io.read(0x04)  # Entries
        data_offset_b = xpk_io.read(0x04)  # Offset of where data is
        archive_size_b = xpk_io.read(0x04)  # Size of this archive
        files_in_folder_1_b = xpk_io.read(0x04)  # Amount of files in folder 1
        files_in_folder_2_b = xpk_io.read(0x04)  # Amount of files in folder 2
        idk_b = xpk_io.read(0x08)  # Padding?

        entries = struct.unpack('<I', entries_b)[0]
        data_offset = struct.unpack('<I', data_offset_b)[0]  # Unused
        archive_size = struct.unpack('<I', archive_size_b)[0]  # Unused
        files_in_folder_1 = struct.unpack('<I', files_in_folder_1_b)[0]  # Unused for now
        files_in_folder_2 = struct.unpack('<I', files_in_folder_2_b)[0]  # Unused for now

        data_entries = []
        for i in range(entries):
            entry_data = xpk_io.read(0x60)
            entry_io = io.BytesIO(entry_data)
            entry = read_entry(entry_io)
            entry_io.close()

            data_entries.append(entry)
            continue

        if idk_b != b'\x00\x00\x00\x00\x00\x00\x00\x00':  # This might be padding, but it might be used for something else?
            print('SOMETHING SPECIAL HAPPENED!')
            breakpoint()
            pass

        for data_entry in data_entries:
            xpk_io.seek(struct.unpack('<I', data_entry.offset)[0])
            data = xpk_io.read(struct.unpack('<I', data_entry.len_)[0])

            fp: str = output + constants.FILE_PATH_SEPARATOR + (xpk_file[xpk_file.index(constants.FILE_PATH_SEPARATOR) + 1:]) + constants.FILE_PATH_SEPARATOR + data_entry.path
            path = fp[:fp.rindex('\\')]

            if not os.path.exists(path):
                os.makedirs(path)
                pass

            if os.path.exists(fp):
                print('File \"{}\" already exists!'.format(fp))
                continue

            stream = open(fp, 'xb+')
            stream.write(data)
            stream.close()

            print('Extracted entry file \"{}\"'.format(fp))
            continue

        xpk_io.close()

        print('Done reading file \"{}\"!\n'.format(xpk_file))
        continue
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='i', required=True, nargs=1, type=str,
                        help='Input folder(s) containing dpk/spk files')
    parser.add_argument('--output', dest='o', required=True, nargs=1, type=str, help='Output folder')
    args = parser.parse_args()

    _input = args.i[0]
    output = args.o[0]

    if not os.path.exists(_input):
        print('Input folder \"{}\" not exist!'.format(_input))
        return

    xpk_files = find_files(_input)
    read_xpk_files(xpk_files, output)
    return


if __name__ == '__main__':
    main()
    pass
