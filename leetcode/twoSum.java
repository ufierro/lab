import java.util.*;
public class MyClass{

    public static void main(String[] args){
        final byte goal = 9;
        final int[] numbers = {  2, 3, 5, 7, 8, 11, 6 };
        int[] result = twoSum(numbers, goal);
        for(int s : result){
            System.out.println(Integer.toString(s));
        }
    }
    
    static int[] twoSum(int[] nums, int goal){
        */
        *  This solution is just me studying a popular and pretty slick solution
        *  available out there, instead of traversing the array a number of times 
        *  you create a HashMap, you store the remainder from substracting the value
        *  of the integer at the given position in the array from the goal integer,
        *  also every iteration checks if the HashMap already contains a key that is 
        *  the value of the integer at that position in the array, effectively finding
        *  the solution to the problem in o(1) time 
        /*
        Map<Integer, Integer> cuenta = new HashMap<Integer, Integer>();
        int size = nums.length;
        for(int i = 0; i <= size; i++){
            if(cuenta.containsKey(nums[i])){
                System.out.println("Found key");
                int primerIndice = cuenta.get(nums[i]);
                System.out.println(Integer.toString(cuenta.get(nums[i])) + " " + Integer.toString(i));
                return new int[]{primerIndice, i};
            }
            System.out.println(Integer.toString(goal-nums[i]) + " " + Integer.toString(i));
            // This is the important bit, we're storing the needed value to reach the goal
            // as a key in the HashMap by substracting from the goal so any integer at any following
            // position which value matches the key is effectively a correct answer
            cuenta.put(goal - nums[i], i);
        }
        return null;
    }
    
}
