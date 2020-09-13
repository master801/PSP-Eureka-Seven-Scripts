meta:
  title: 'DPK/SPK for Eureka Seven PSP'
  id: xpk
  endian: le
  file-extension:
    - dpk
    - spk
seq:
  - id: magic
    type: magic
    size: 0x04
    doc: 'Magic'
  - id: amnt_of_entries
    type: u4
    doc: 'Amount of files this archive contains'
  - id: start_data_offset
    type: u4
    doc: 'The offset at which data starts. Usually 0x80'
  - id: archive_size
    type: u4
    doc: 'Size of this archive file'
  - id: files_in_folder_1
    type: u4
    doc: 'Amount of files in folder 1'
  - id: files_in_folder_2
    type: u4
    doc: 'Amount of files in folder 2'
  - id: idk
    size: 0x08
    doc: 'Padding?'
  - id: entries
    type: entry
    repeat: expr
    repeat-expr: entry_len
    size: 0x60
types:
  magic:
    seq:
      - id: magic
        size: 0x04
        contents: [0x74, 0xD6, 0x40, 0x00]
        doc: 'Magic'
  entry:
    seq:
      - id: off
        type: u4
      - id: len
        type: u4
      - id: idk3
        type: u4
      - id: idk4
        type: u4
      - id: idk5
        type: u4
      - id: idk6
        type: u4
      - id: idk7
        type: u4
      - id: idk8
        type: u4
      - id: name
        type: strz
        include: false
        size-eos: false
        encoding: UTF-8
      - id: idk9
        type: u4
      - id: idk10
        type: u4
      - id: idk11
        type: u4
      - id: idk12
        type: u4
      - id: idk13
        type: u4
      - id: idk14
        type: u4
      - id: idk15
        type: u4
      - id: idk16
        type: u4
      - id: idk17
        type: u4
      - id: idk18
        type: u4