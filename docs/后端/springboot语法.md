## 语法

1.@Controller 针对类
```
@Controller
public class OmsOrderController {

}
```

2.@ResponseBody
@RequestMapping
@RequestParam 
@RequestBody
@PathVariable
```
@ResponseBody
@RequestMapping(value = "/{id}", method = RequestMethod.POST)
public String list(@RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam("ids") List ids, @RequestBody List list, @PathVariable Long id) {  //请求参数
  return 'xx'
}
```

3.查

@RequestMapping()
@ResponseBody
public CommentResult<Order> list() {
  
}
