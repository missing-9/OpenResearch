import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author kylin
 */
@Component
@Slf4j
public class AccessInterceptor implements HandlerInterceptor {

    /**
     * 在请求已经返回之后执行
     * @param request
     * @param response
     * @param handler
     * @param ex
     * @throws Exception
     */
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
    }

    /**
     * 执行目标方法之后执行
     * @param request
     * @param response
     * @param handler
     * @param ex
     * @throws Exception
     */
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView ex) throws Exception {
    }

    /**
     * 在执行目标方法之前执行
     * @param request
     * @param response
     * @param handler
     * @return
     * @throws Exception
     */
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
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
    }
}