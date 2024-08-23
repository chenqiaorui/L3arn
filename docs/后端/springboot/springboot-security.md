1. springboot-security 用于实现认证授权。

2. 用到的数据表

- sys_user    用户名和密码
- sys_role      角色名称
- sys_menu 权限表   菜单名称
- sys_user_role   
- sys_role_menu

3. 依赖
   - springboot
   - spring-security
   - mybatis-plus
   - jdk1.8
   - lombok
   - druid
   - mysql
   - fastjson
   - spring-security-jwt
     
4. 接口
   - login
   - userinfo

5. 实现逻辑
5.1 实现UserDetails接口，UserDetails用于记录用户的信息，包括认证和授权：public class SelfUserEntity implements Serializable, UserDetails
5.2 创建token：createAccessToken，传入实现UD的实体类：根据用户id/用户名/签发时间/签发着/用户权限生成token
5.3
   编写暂无权限处理类

   编写用户未登录处理类

   编写登录失败处理类

   编写登录成功处理类

   编写登出成功处理类

   编写自定义登录验证类

   编写自定义权限验证

   编写SpringSecurity核心配置类

   编写JWT接口请求校验拦截器
   
   

7. 

参考：https://juejin.cn/post/6844903974546456590?searchId=202408210937075D7AFE3DFC9F753954CE
