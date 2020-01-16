# jackpot

## 接口文档

### /home/index 首页

参数名|描述|是否必须
---|:--:|---:
category|游戏分类（用于展示导航）默认ALL|否
gameid|游戏id（用于展示赛事）默认ALL|否

```
  {
	data: {
		banners: [{
				pic: "",
				url: ""
			},
			{
				pic: "",
				url: ""
			},
			{
				pic: "",
				url: ""
			}
		],
		games: [{
				gameid: "",
				icon: "",
				name: ""
			},
			{
				gameid: "",
				icon: "",
				name: ""
			},
			{
				gameid: "",
				icon: "",
				name: ""
			}
		],
		match: [{
				icon: "",
				live_url: "",
				matchid: "",
				players: [{
						icon: "",
						name: "",
						odds: ""
					},
					{
						icon: "",
						name: "",
						odds: ""
					}
				],
				start_time: "1579192268",
				sub_title: "",
				title: ""
			},
			{
				icon: "",
				live_url: "",
				matchid: "",
				players: [{
						icon: "",
						name: "",
						odds: ""
					},
					{
						icon: "",
						name: "",
						odds: ""
					}
				],
				start_time: "1579192268",
				sub_title: "",
				title: ""
			},
			{
				icon: "",
				live_url: "",
				matchid: "",
				players: [{
						icon: "",
						name: "",
						odds: ""
					},
					{
						icon: "",
						name: "",
						odds: ""
					}
				],
				start_time: "1579192268",
				sub_title: "",
				title: ""
			}
		]
	},
	ec: 200,
	em: "OK"
  }
```

-----------


### /bet/rules 下注规则

参数名|描述|是否必须
---|:--:|---:
matchid|赛事id|是

```
  {
	data: {
		icon: "",
		players: [{
				icon: "",
				name: ""
			},
			{
				icon: "",
				name: ""
			}
		],
		rules: [{
				rules: [{
						desc: "",
						odds: "",
						ruleid: ""
					},
					{
						desc: "",
						odds: "",
						ruleid: ""
					}
				],
				text: ""
			},
			{
				rules: [{
						desc: "",
						odds: "",
						ruleid: ""
					},
					{
						desc: "",
						odds: "",
						ruleid: ""
					}
				],
				text: ""
			}
		],
		start_time: "1579192268",
		sub_title: "",
		title: ""
	},
	ec: 200,
	em: "OK"
}
```

-----------


### /bet/bet 下注

参数名|描述|是否必须
---|:--:|---:
matchid|赛事id|是
ruleid|规则id|是
amount|金额|是

```
  {
	data: {},
	ec: 200,
	em: "OK"
}
```
