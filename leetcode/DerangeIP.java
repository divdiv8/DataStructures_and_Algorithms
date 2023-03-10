//https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution {
    public String defangIPaddr(String address) {
        String[] strSplit = address.split("");
  
        // Now convert string into ArrayList
        ArrayList<String> strList = new ArrayList<String>(
            Arrays.asList(strSplit));
        String strList2 ="";
        //System.out.println(strList2+"strList2");
        // Now print the ArrayList
        for (int i = 0; i < strList.size(); i++)
        {
            if(strList.get(i).charAt(0)=='.')
                strList2+="[.]";
            else
                strList2+=strList.get(i).charAt(0);

        }
        return strList2;
    }
}

//one line solution 

class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".","[.]");
    }
}
