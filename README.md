# Eureka Seven PSP Scripts


## Info

Scripts to extract .dpk and .spk files from the PSP game `Eureka Seven V.2: Psalms of Planets`.<br/>
Note that .dpk files only contain textures and models, while .spk files contain sounds and music.<br/>

Please give credit where it's due if using this tool.<br/>


## Usage

#### Arguments:
- `--input` [`INPUT_DIRECTORY`] - Input directory containing .dpk and/or .spk files
- `--output` [`OUTPUT_DIRECTORY`] - Output directory to extract the files to

#### Example usage:
```
python main.py --input="ORIGINAL/data2" --output=EXTRACTED
```

#### Tested on:
- Windows (Windows 10)

### Currently Supports:
- [x] Extraction
- [ ] Insertion
