## mock数据

1. 新建文件 db.json
```   
{
  "items": ["事项 A", "事项 B", "事项 C"]
}
```
2. 在db.json当前文件下执行

npx json-server db.json

3.访问

localhost:3000/items
4. other

timeline.json

```
{
"data": {
	"err_code": 0,
	  "err_msg": "success",
	  "data": [
		  {
			  "id": "41",
			  "nickname":"Bob Brown",
			  "avatar":"01",
			  "text": "Behind every successful man there's a lot u unsuccessful years. http://goo.gl/",
			  "original_pic": "",
			  "created_at": "1404709434"
		  },
		  {
			  "id": "40",
			  "nickname":"Jean Kerr",
			  "avatar":"07",
			  "text": "I think success has no rules, but you can learn a lot from failure. ",
			  "original_pic": "",
			  "created_at": "1404708544"
		  },
		  {
			  "id": "39",
			  "nickname":"Colin L. Powell",
			  "avatar":"03",
			  "text": "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. www.youtube.com ",
			  "original_pic": "",
			  "created_at": "1404708455"
		  },
		  {
			  "id": "38",
			  "nickname":"Balzac",
			  "avatar":"05",
			  "text": "There is no such thing as a great talent without great will - power.",
			  "original_pic": "style/img/sample_01.jpg",
			  "created_at": "1404707590"
		  },
		  {
			  "id": "37",
			  "nickname":"Charles Chaplin",
			  "avatar":"07",
			  "text": "You have to believe in yourself. That's the secret of success.",
			  "original_pic": "",
			  "created_at": "1404707580"
		  },
		  {
			  "id": "36",
			  "nickname":"R.M. Nixon",
			  "avatar":"04",
			  "text": "Our destiny offers not the cup of despair, but the chalice of opportunity. So let us seize it, not in fear, but in gladness.",
			  "original_pic": "",
			  "created_at": "1404707197"
		  },
		  {
			  "id": "35",
			  "nickname":"Erasmus",
			  "avatar":"08",
			  "text": "None is of freedom or of life deserving unless he daily conquers it anew.",
			  "original_pic": "style/img/sample_02.jpg",
			  "created_at": "1404706070"
		  },
		  {
			  "id": "34",
			  "nickname":"John Ruskin",
			  "avatar":"03",
			  "text": "Living without an aim is like sailing without a compass.",
			  "original_pic": "",
			  "created_at": "1404706060"
		  },
		  {
			  "id": "33",
			  "nickname":"George Eliot",
			  "avatar":"06",
			  "text": "What makes life dreary is the want of motive.",
			  "original_pic": "style/img/sample_03.jpg",
			  "created_at": "1404705260"
		  },
		  {
			  "id": "32",
			  "nickname":"Lincoln",
			  "avatar":"06",
			  "text": "Towering genius disdains a beaten path. It seeks regions hitherto unexplored.",
			  "original_pic": "",
			  "created_at": "1404705240"
		  },
		  {
			  "id": "31",
			  "nickname":"Erasmus",
			  "avatar":"10",
			  "text": "None is of freedom or of life deserving unless he daily conquers it anew. ",
			  "original_pic": "",
			  "created_at": "1404705133"
		  },
		  {
			  "id": "30",
			  "nickname":"Thomas Addison",
			  "avatar":"10",
			  "text": "A strong man will struggle with the storms of fate.",
			  "original_pic": "",
			  "created_at": "1404704742"
		  }
	  ]
	}
}
```

5. more json files check : https://github.com/BelinChung/HiApp/tree/grunt/src/api
