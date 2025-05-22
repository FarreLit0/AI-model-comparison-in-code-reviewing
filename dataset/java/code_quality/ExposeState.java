
import java.util.HashMap;

public class ExposeState {
    private HashMap<String, String> config = new HashMap<>();

    public HashMap<String, String> getConfig() {
        return config;
    }

    public void setValue(String key, String value) {
        config.put(key, value);
        writerConfig();
    }
}
