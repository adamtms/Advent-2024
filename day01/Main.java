import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    static ArrayList<ArrayList<Integer>> readFile() {
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();
        File myFile = new File("input.txt");
        try {
            Scanner scanner = new Scanner(myFile);
            while (scanner.hasNextLine()) {
                String data = scanner.nextLine();
                String[] elements = data.split(" +");
                left.add(Integer.parseInt(elements[0]));
                right.add(Integer.parseInt(elements[1]));
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
        ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>();
        output.add(left);
        output.add(right);
        return output;
    }

    static void task1() {
        ArrayList<ArrayList<Integer>> columns = readFile();
        ArrayList<Integer> left = columns.get(0);
        ArrayList<Integer> right = columns.get(1);
        Collections.sort(left);
        Collections.sort(right);
        int sum = 0;
        for (int i=0; i < left.size(); i++) {
            sum += Math.abs(left.get(i) - right.get(i));
        }
        System.out.println(sum);
    }

    static void task2() {
        ArrayList<ArrayList<Integer>> columns = readFile();
        ArrayList<Integer> left = columns.get(0);
        ArrayList<Integer> right = columns.get(1);
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (Integer element: right) {
            Integer value = counter.get(element);
            if (value == null) {
                value = 0;
            }
            counter.put(element, value + 1);
        }
        int sum = 0;
        for (Integer element: left) {
            Integer value = counter.get(element);
            if (value == null) {
                continue;
            }
            sum += value * element;
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {
        task1();
        task2();
    }
}