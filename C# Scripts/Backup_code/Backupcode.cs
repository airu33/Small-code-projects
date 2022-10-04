using System;

namespace app
{
    public static class Program
    {

        class Globals
        {
            public static int loopTime;
            public static string? src;
            public static string? dst;
        }      
        public static void DeletOldFolder()
        {
            if(Directory.Exists(Globals.dst))
            {
                Directory.Delete(Globals.dst, true);
                Console.WriteLine("dst replaced");
            }
            else
            {
                Console.WriteLine("dst does not exist"); 
            }
        }
        public static void Main(string[] args)
        {
            Console.WriteLine("loopTime is the amount of seconds between copies");
            Globals.loopTime = Convert.ToInt32(Console.ReadLine()); /**/

            Console.WriteLine("src is the sorce file you whant to copie example C:/Users/Name/Desktop/Folder");
            Globals.src = Console.ReadLine();

            Console.WriteLine("dst is the destination folder you whant to copie to example C:/Users/Name/Desktop/Folder");
            Globals.dst = Console. ReadLine();


            Console.WriteLine(Globals.loopTime);
            Console.WriteLine(Globals.src);

           
            for (int t = Globals.loopTime; t >= 0; t--)
            {
                Console.WriteLine("\rNext Backup in {0:00}", t);
                System.Threading.Thread.Sleep(1000);
                if(t == 0)
                {                  
                    DeletOldFolder();

                    t = Globals.loopTime;
                }
            }
        }
    }
}