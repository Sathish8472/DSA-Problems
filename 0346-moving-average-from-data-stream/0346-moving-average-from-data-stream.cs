public class MovingAverage {
    int _window_size;
    List<int> nums = new List<int>();
    double result = 0;
    int left = 0;
    int count = 0;

    public MovingAverage(int size) {
        _window_size = size;
    }
    
    public double Next(int val) {
        nums.Add(val);
        count++;
        
        Console.WriteLine($"count: {count},_window_size: {_window_size}, result: {result} ");

        Console.WriteLine($"val: {val}");
        if(count > _window_size){
            int removeVal = nums[left];
            left++;
            result -= removeVal;
            count--;
        }

        Console.WriteLine($"result: {result}");
        result += val;

        return result / count;
    }


}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.Next(val);
 */