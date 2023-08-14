# Are-U-Poisonous-Snake

本レポジトリは知能情報総合実験・データマイニング班 G2により作成されました。

## 環境構築

pipによる依存関係のインストールを行なってください。

```bash
pip install -r requirements.txt
```

## データセットを準備

G2により、まとめたデータセット[datasets](https://gitlab.ie.u-ryukyu.ac.jp/e215742/datasets)のインストールをしてください。

```bash
git clone https://gitlab.ie.u-ryukyu.ac.jp/e215742/datasets.git
```

次に、ファイルをこのように配置してください。

```bash
.
├── README.md
├── experiment1
│   └── ex1Tutorial.ipynb
│   └── snake_images
├── experiment2
│   └── ex2Fine_chuning.ipynb
│   └── dataset1
├── experiment3
│   └── ex3Fine_chuning.ipynb
│   └── dataset2
├── experiment4
│   ├── unittest.py
│   └── fine_chuning_vgg16.py
│   └── dataset3
│   └── snake-dataset-indian
├── requirements.txt
└── usemodel
    └── usemodel.ipynb
    └── snake-dataset-indian
```

## 実行方法

`*.ipynb` ファイルの場合

```bash
jupyter notebook path/to/*.ipynb
```

python ファイルの場合

```bash
python3 fine_chuning_vgg16.py  --train-directory-path /path/to/train_dir --test-directory-path /path/to/test_dir
```

## 実行において生成されるファイル

`*.ipynb`の場合は下記のファイルが生成される。

```bash
models/snake_poisonClassifier1.h5 # ex1Tutorial.ipynb のあるディレクトリに生成される

models/snake_poisonClassifierFC1.h5 # ex2Fine_chuning.ipynbのあるディレクトリに生成される

models/snake_poisonClassifierFC2.h5 # ex3Fine_chuning.ipynbのあるディレクトリに生成される
```

`experiment4`以下には下記のファイルが生成される。

```bash
# モデルの学習において生成される
./train_accracy.png # 学習に対しての正解率
./train_loss.png # 学習に対しての損失
./train_test_result.txt # 学習に用いたデータセットに対しての耐性を保存している

# 別で読み込んだデータセットを用いたモデルの評価において生成される
./test_result.txt

# モデルの保存で生成される
./models/imageclassifier_VGG16.h5 # h5形式で保存される
```

上記に加えて、それぞれに`logs` がつくられ`train`,`validation` のログを生成する。
