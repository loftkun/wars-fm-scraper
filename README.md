wars-fm-scraper
==================================================

# What it is?
scrape record of game from [wars.fm](http://wars.fm/)

| game | record of game | url                                          | app title                      |
|:----:|:--------------:|:--------------------------------------------:|:------------------------------:|
| shogi | *.csa         | [http://wars.fm/shogi](http://wars.fm/shogi) | Shogi Quest ( 将棋クエスト )   |
| go    | *.sgf         | [http://wars.fm/go9](http://wars.fm/go9)     | Go Quest ( 囲碁クエスト )      |
| renju | *.sgf         | [http://wars.fm/renju](http://wars.fm/renju) | Renju Quest ( 五目クエスト )   |


# Getting Started
## Prerequisites
- Google Chrome( > 59.0 )  
- Python3.x  
- selenium ( python binding )  
- chromedriver  

### installation example
#### for Ubuntu 14

##### Google Chrome  
```bash
$ sudo apt-get install libappindicator1 fonts-liberation
$ sudo apt-get install xdg-utils libxss1
$ 
$ curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ 
$ # if required
$ sudo apt-get install -f
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ 
$ # check version
$ google-chrome --version
Google Chrome 64.0.3282.167
```
<br>
##### selenium ( python binding )    
```bash
$ pip3 install selenium
```
<br>
##### chromedriver  
If you want latest version, get from below.
[https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
```bash
$ wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/local/bin/
```
<br>
## Usage
```bash
$ ./wars-fm-scraper.py ${url} ${filepath}
```

### example
#### Shogi Quest ( 将棋クエスト ) 
```bash
$ ./wars-fm-scraper.py http://wars.fm/shogi10?gameId=r0jo2gocc27f#game/r0jo2gocc27f test.csa
get : http://wars.fm/shogi10?gameId=r0jo2gocc27f#game/r0jo2gocc27f
saved : test.csa
$ cat ./test.csa
'Shogi Quest
N+loftkun(1632)
N-testuser(1769)
P1-KY-KE-GI-KI-OU-KI-GI-KE-KY
P2 * -HI *  *  *  *  * -KA *
P3-FU-FU-FU-FU-FU-FU-FU-FU-FU
P4 *  *  *  *  *  *  *  *  *
P5 *  *  *  *  *  *  *  *  *
P6 *  *  *  *  *  *  *  *  *
P7+FU+FU+FU+FU+FU+FU+FU+FU+FU
P8 * +KA *  *  *  *  * +HI *
P9+KY+KE+GI+KI+OU+KI+GI+KE+KY
+
+7776FU
-3334FU
+6766FU
-5354FU
( Abbreviation )
-0065KY
+5241TO
-3222OU
+4131TO
$

```
#### Go Quest ( 囲碁クエスト ) / Renju Quest ( 五目クエスト )
```bash
$ ./wars-fm-scraper.py http://wars.fm/go9?gameId=ihl3v3uu7thy#game/ihl3v3uu7thy hoge.sgf
get : http://wars.fm/go9?gameId=ihl3v3uu7thy#game/ihl3v3uu7thy
saved : hoge.sgf
$ cat ./hoge.sgf
(;GM[1]SZ[9]KM[7.0]RU[Chinese]
PB[:Aya5Bot(1969)]
PW[testuser(2073)]
;B[dd];W[gf];B[dg];W[fc];B[fd];W[gd];B[fe];W[ge];B[ec];W[cg];B[cf];W[bf];B[ch];W[bg];B[ce];W[be];B[bd];W[bh];B[dh];W[bc];B[ae];W[cc];B[cd];W[ab];B[db];W[ad];B[ac];W[ba];B[cb];W[ad];B[fb];W[bb];B[ac];W[ef];B[ad];W[df];B[eg];W[ff];B[bi];W[fg];B[ah];W[gc];B[gb];W[hb];B[ha])
$
```

