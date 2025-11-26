public class Solution{
    public int MaximumUnits(int[][] boxTypes, int truckSize)
    {
        var sorted = boxTypes.OrderByDescending(b => b[1]);

        var totalUnits = 0;

        foreach(var box in sorted){
            var boxCount = box[0];
            var unitsPerBox = box[1];

            var boxesToTake = Math.Min(truckSize, boxCount);

            totalUnits += boxesToTake * unitsPerBox;
            truckSize -= boxesToTake;

            if (truckSize == 0) break;
        }
        
        return totalUnits;
    }
}