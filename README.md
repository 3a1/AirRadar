# RadarSky

To record ads-b frequency:
```bash
$ hackrf_transfer -r --f 1090000000 -s 2000000 -p 0 -a 0 -l 40 -g 62
```

Change file encoding:
```bash
$ sox --rate 2000000 --channels 1 --type sb - --type ub -
```

Get ads-b sygnals:
```bash
$ ./ads-b data.txt
```

Get airplanes position visualisation:
```bash
$ ./dump1090 --ifile data.txt --net
```


<details>
           <summary>Photos</summary>
           ![image](https://github.com/Zebra64/RadarSky/assets/75133897/7817bb67-5763-4cfb-b647-642ac7910c09)
           ![image](https://github.com/Zebra64/RadarSky/assets/75133897/d5c90803-240f-4fc6-8fd5-7fadc95327e8)
</details>
