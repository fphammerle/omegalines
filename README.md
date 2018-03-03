# omegalines

python script to use onion omega with oled expansion as
a **departure monitor** for the **public transport** service in **Vienna/Austria**
supporting *Wiener Linien* and *ÖBB*

![oled display](pictures/20180216T130230.jpg)

## Hardware

[onion omega2](https://onion.io/omega2/)

[onion oled expansion](https://onion.io/store/oled-expansion/)

## Configuration

See [sample config](config-sample.yml) for details

```yaml
wiener_linien:
  api_key: a1b2c3d4e5f6
  update_interval_seconds: 7
  rbl: 4648
oebb:
  eva_ids: [8101934, 8101947]
  update_interval_seconds: 17
offset_seconds: 60
```
