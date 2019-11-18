
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;

/**
 *
 * @author kylin
 */
public class Main {
    public static void main(String[] args) throws Exception{
        CloseableHttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet httpGet = new HttpGet("http://localhost:7000/api/exportClue");
        CloseableHttpResponse  response = httpClient.execute(httpGet);
        System.out.println(response.getEntity());
    }
}