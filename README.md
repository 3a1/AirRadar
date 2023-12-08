<h1 align="center">
  <br>
  <a href="https://github.com/3a1/AirRadar"><img src="https://i.imgur.com/wExC4Tc.png" alt="AirRadar" width="200"></a>
  <br>
  AirRadar
  <br>
</h1>

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-red">
</div>

![image](https://github.com/Zebra64/RadarSky/assets/75133897/fbce5d1c-6ff3-48e2-b67a-6233fa1a6c54)


To record ads-b frequency:
```bash
$ hackrf_transfer -r data -f 1090000000 -s 2000000 -p 0 -a 0 -l 40 -g 62
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
