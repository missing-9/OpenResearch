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
     * �������Ѿ�����֮��ִ��
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
     * ִ��Ŀ�귽��֮��ִ��
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
     * ��ִ��Ŀ�귽��֮ǰִ��
     * @param request
     * @param response
     * @param handler
     * @return
     * @throws Exception
     */
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        //�ж��Ƿ񷽷������
        if (handler instanceof HandlerMethod) {
            HandlerMethod handlerMethod = (HandlerMethod) handler;
            AccessExportClue accessExportClue = handlerMethod.getMethodAnnotation(AccessExportClue.class);
            //��ע��,����Ȩ�޵���Ŀ�귽��
            if (accessExportClue != null) {
                return true;
            }
        }

        String token = request.getHeader("auth");
        if (StringUtils.isBlank(token)) {
            throw new SkbNoAccessPermissionException("δ��¼ token  is null.");
        }
        return true;
    }
}