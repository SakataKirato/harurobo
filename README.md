# 説明
これはコントローラでodriveを動かせるようにしたものです、ノードごとにターミナルが開くようになっています
## つかいかた
まず以下を打ちノード起動時ターミナルを複数開くようにする
```
sudo apt update
sudo apt install xterm
```
次に[haru_odrive](https://github.com/nokaaaaa/haru_odrive)を参考にしキャリブしてconfig.jsonを書く</br>
次にjoy_translate_node.pyの15行目のfile_pathを自身のconfig.yamlのpathに書き換える</br>
必要に応じてconfig.yamlの数値も変える</br>
ビルドソースし、コントローラをパソコンにつなぎ以下のように打つ　　
```
ros2 launch haru_launch haru_launch.py config_file:=[config.jsonのpath] ls:=[直進移動の速度係数] as:=[旋回移動の速度係数]
```

抜けがあったらごめんなさい
