---
typora-copy-images-to: ./
---

```
1，定义注解接口，@interface AccessExportClue，指明注解作用于方法上（@Target(ElementType.METHOD)）

2，实现接口（AccessInterceptor.java），实现逻辑写在preHandle里。

​```java
        //判断是否方法级别的
        if (handler instanceof HandlerMethod) {
            HandlerMethod handlerMethod = (HandlerMethod) handler;
            AccessExportClue accessExportClue = handlerMethod.getMethodAnnotation(AccessExportClue.class);
            //有注解,则有权限调用目标方法
            if (accessExportClue != null) {
                return true;
            }
        }

        String token = request.getHeader("auth");
        if (StringUtils.isBlank(token)) {
            throw new SkbNoAccessPermissionException("未登录 token  is null.");
        }
        return true;
​```

3，拦截进api的请求，让注解发挥作用。（AccessConfigure.java）

​```java
        registry.addInterceptor(accessInterceptor).addPathPatterns("/**");
        super.addInterceptors(registry);
​```
4，使用注解。（AccessExportController.java）

4.1，未使用注解前：

​```java
@RestController
public class AccessExportController {

    @GetMapping(value = "/exportClue")
    public ResultResponse exportClue(){

        return new ResultResponse(0,true,"access to export clue",null);
    }

}
​```
![未使用注解](C:\Users\Administrator\Desktop\annotation\未使用注解.png)

4.2，使用注解后：

​```java
    @AccessExportClue
    @GetMapping(value = "/exportClue")
    public ResultResponse exportClue(){

        return new ResultResponse(0,true,"access to export clue",null);
    }
​```
![使用注解](C:\Users\Administrator\Desktop\annotation\使用注解.png)

注解正确起作用。
```