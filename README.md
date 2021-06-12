# KakeEnMono
![ScreenShot](https://user-images.githubusercontent.com/67098414/121771613-57ee1900-cbab-11eb-929e-1f42c4c1ebb9.jpg)
日本語対応のプログラミング用フォント

"KakeEn" は「駆け出しエンジニア」から来ています。

## Features
ベースは、

* Ubuntu Mono
* 源柔ゴシック(等幅)

です。

英字はUbuntu Mono、その他は源柔ゴシックという構成になっています。

また、それぞれのフォントがいい感じになるように調整してあります。

さらに、Rictyを参考に全角スペースを可視化するようにしました。

## How to Build
### Requirements
フォントを生成するにあたり、fontforgeが必要です。

Ubuntuなら、

```
sudo apt-get install fontforge
```

です。

環境に合わせてインストールしてください。

### Building
まずは、このリポジトリをクローンしてください。

```
git clone https://github.com/laddge/KakeEnMono.git KakeEnMono
```

次に、ベースとなるフォントをダウンロードしてください。

* [Ubuntu Mono](https://fonts.google.com/specimen/Ubuntu+Mono)
* [源柔ゴシック](http://jikasei.me/font/genjyuu/)

それぞれ解凍して、次の場所に置いてください。

```
KakeEnMono
├── fonts
│   ├── GenJyuuGothic-Monospace-Regular.ttf
│   └── UbuntuMono-Regular.ttf
...
```

そして、ビルドスクリプトを走らせます。

```
cd KakeEnMono
./generator
```

すると、先程フォントを配置したディレクトリに、`KakeEnMono-Regular.ttf`が生成されているはずです。

必要に応じて、Powerlineなどのパッチを当てるといいかもしれません。

## LICENCE
このフォントの生成スクリプトはMITライセンスです。([LICENCE](LICENCE)をご覧ください)

ベースのフォントはそれぞれライセンスが違うため、フォントを配布することはできません。

生成されたいかなるものについても、再配布を禁止します。

## Author
Laddge
