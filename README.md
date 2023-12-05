# RadarSky

To record ads-b frequency:
```bash
$ hackrf_transfer -r data --f 1090000000 -s 2000000 -p 0 -a 0 -l 40 -g 62
```

Change file encoding:
```bash
$ sox --rate 2000000 --channels 1 --type sb data --type ub datasorted
```

Get ads-b sygnals:
```bash
$ ./ads-b datasorted
```

Get airplanes position visualisation:
```bash
$ drawDefault.py data.txt
```

<details>
           <summary>Photos</summary>
           <p>
           <img src="https://github.com/Zebra64/RadarSky/assets/75133897/d5c90803-240f-4fc6-8fd5-7fadc95327e8"></img>
           <img src="https://github.com/Zebra64/RadarSky/assets/75133897/7817bb67-5763-4cfb-b647-642ac7910c09"></img>
           </p>
</details>
