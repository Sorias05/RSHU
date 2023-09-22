using System.Text;

namespace Lab4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            BinaryTree tree = new BinaryTree();//створюємо порожнє дерево
            tree.Root = new TreeNode(1);//задаємо головний вузол (корінь) дерева
            tree.Root.Left = new TreeNode(2);//задаємо лівий вузол головного вузла
            tree.Root.Left.Left = new TreeNode(5);//задаємо лівий вузол вузла 2
            tree.Root.Left.Left.Left = new TreeNode(10);
            tree.Root.Left.Left.Right = new TreeNode(11);
            tree.Root.Left.Right = new TreeNode(4);//задаємо правий вузол вузла 2
            tree.Root.Left.Right.Left = new TreeNode(9);
            tree.Root.Left.Right.Right = new TreeNode(8);
            tree.Root.Right = new TreeNode(3);//задаємо правий вузол головного вузла
            tree.Root.Right.Left = new TreeNode(6);//задаємо лівий вузол вузла 6
            tree.Root.Right.Left.Right = new TreeNode(12);
            tree.Root.Right.Right = new TreeNode(7);//задаємо правий вузол вузла 6
            tree.Root.Right.Right.Right = new TreeNode(13);
            List<int> bpath = tree.FindPath(13);//шукаємо шлях до 13 вузла, і поміщаємо маршрут в список bpath
            if (bpath.Count > 0)//якщо список не порожній, значить маршрут існує
            {
                Console.Write("Шлях: ");//виводимо шлях до нього
                foreach (int nodeName in bpath)//для кожного елемента в списку маршруту
                {
                    Console.Write(nodeName + " ");//виводимо вузол і додаємо пробіл
                }
                Console.WriteLine();//переходимо на рядок вниз
            }
            else//якщо список порожній, то шляху не існує
            {
                Console.WriteLine("Не знайдено вузла з таким значенням.");//виводимо повідомлення, що маршруту немає
            }
            //чекаємо поки користувач натисне любу клавішу на клавіатурі
            Console.ReadKey();
        }
    }
}