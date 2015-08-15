public class Main {

    public static void main(String[] args) {
        java.util.Scanner in = new java.util.Scanner(System.in);
        Clock clock = new Clock(in.nextInt(), in.nextInt(), in.nextInt());
        clock.tick();
        System.out.println(clock);
        in.close();
    }

}

class Display {

    private int limit;
    private int value;

    public Display(int limit) {
        this.limit = limit;
    }
    public void increase() {
        this.value++;
        if (this.value == this.limit) {
            this.value = 0;
        }
    }
    public void set(int val) {
        this.value = val;
    }
    public int get() {
        return this.value;
    }

}

class Clock {

    private Display hour = new Display(24);
    private Display minute = new Display(60);
    private Display second = new Display(60);

    public Clock(int hour, int minute, int second) {
        this.hour.set(hour);
        this.minute.set(minute);
        this.second.set(second);
    }

    public void tick() {
        this.second.increase();
        if (this.second.get() == 0) {
            this.minute.increase();
            if (this.minute.get() == 0) {
                this.hour.increase();
            }
        }
    }

    public String toString() {
        return String.format("%02d:%02d:%02d", this.hour.get(), this.minute.get(), this.second.get());
    }

}
