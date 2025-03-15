namespace DefaultNamespace;

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        Dictionary<char, bool> charPresence = new Dictionary<char, bool>();
        int maxNumber = 0;
        
        for (int i = 0; i < s.Length; i++)
        {
            int number = 0;
            int index = i;
            while (index < s.Length)
            {
                if (!charPresence.TryGetValue(s[index], out _))
                {
                    charPresence.Add(s[index], true);
                    number++;
                }
                else
                {
                    break;
                }

                index++;
            }
            charPresence.Clear();
            if (number > maxNumber)
            {
                maxNumber = number;
            }
        }

        return maxNumber;
    }
}