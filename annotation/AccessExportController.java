import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author kylin
 */
@RestController
public class AccessExportController {

    @AccessExportClue
    @GetMapping(value = "/exportClue")
    public ResultResponse exportClue(){

        return new ResultResponse(0,true,"access to export clue",null);
    }

}