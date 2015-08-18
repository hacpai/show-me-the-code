import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        CItyMap citymap = new CItyMap();
        citymap.addCity();
        citymap.addDist();
        System.out.println(citymap.queryDist());
    }

}

class CItyMap {

    ArrayList<String> citys = new ArrayList<String>();
    HashMap<String, Integer> dist = new HashMap<String, Integer>();
    Scanner in = new java.util.Scanner(System.in);

    public void addCity() {
        String city = in.next();
        while (!city.equals("###")) {
            citys.add(city);
            city = in.next();
        }
    }

    public void addDist() {
        for (String cityx : citys) {
            for (String cityy : citys) {
                int distance = in.nextInt();
                dist.put(cityx + cityy, distance);
            }
        }
    }

    public int queryDist() {
        String cityx = in.next();
        String cityy = in.next();
        return dist.get(cityx+cityy);
    }

}
