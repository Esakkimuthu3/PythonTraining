using system;

namespace MyfirstProgram
{
    class Program
    {

        static void main(string args[])
        {

            Random random = new random();
            bool playAgain = true;
            int min = 1;
            int max = 100;
            int number;
            int guess;
            int guesses;

            while (playAgain)
            {
                guess = o;
                guesses = o;
                number = random.Next(min , max+1);

                while (guess != number)
                {
                    Console.Writeline("Guess a number between:", min, "-",max);

                    guess = Convert.ToInt32(Console.Readline());

                    Console.Writeline("Guess:",guess);

                    if(guess > number)
                    {
                        Console.Writeline("Hight");
                    }
                    else if(guess< number)
                    {

                        Console.Writeline("Low");


                    }

                    guesses++;
                }
                Console.Writeline("You Win");

                response = Console.Readline("Eneter Y/N:").ToUpper();

                if(response == "Y")
                {
                    playAgain = true;
                }


            }

            Console.ReadKey();


        }


    }
}