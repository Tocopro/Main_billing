Main Class

package com.company;

public class Main {


    public static void main(String[] args) {

        Billing consumption = new Billing((float) 5.67,1609,"Maximillian");
        System.out.println("\nThis Month Billing total  wattage consumed is " + (consumption.getConsumption()) + " watts");
        System.out.println("Rate of cost is 5.67 cents per watt");
        System.out.println("Cost of Energy is $" + consumption.getCost());
        System.out.println(consumption.getName() + " bill total for this month: $" + consumption.getCost());

        Billing consumption2 = new Billing(3.45,3245,"Nescafe");
        System.out.println("\nThis Month Billing total wattage consumed is " + consumption2.getWatts() + " watts");
        System.out.println("Rate of cost is 3.45 cents per watt");
        System.out.println("Cost of Energy is $" + consumption2.getCost());
        System.out.println(consumption2.getName() + " bill for this month is $" + consumption2.getCost());

        int difference = consumption.getCost() - consumption2.getCost();


        System.out.println("\nCost difference between the two consumers $" + Math.abs(difference));



    }
}
 
 constructor
 
 package com.company;

public class Billing {

    double watts;
    String name;
    double rate;

    public int getConsumption() {
        return (int) (rate * watts);
    }
    public Billing(double r, double w, String n) {
        watts = w;
        rate = r;
        name = n;
    }
    public  int getCost() {
        return (int) ((watts * rate) / 100);// the cost in dollar unit is the product of
        // watts and rates divided by 100 cents
    }

    public String getName() {
        return name;
    }
    public int getWatts() {
        return (int) watts;
    }
    public int getRate() {
        return (int) rate;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setRate(int rate) {
        this.rate = rate;
    }
    public void setWatts(int watts) {
        this.watts = watts;
    }
}
