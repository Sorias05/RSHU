using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    internal class BinaryTree
    {
        public TreeNode Root = null;//тут будемо зберігати корінь дерева, початковий вузол
        public BinaryTree(TreeNode root)//створення дерева із заданням кореня, початкового вузла дерева
        {
            Root = root;//означуємо корінь дерева
        }
        public BinaryTree() { }//дозволяємо створення дерева без параметрів
                               // Функція для пошуку шляху в бінарному дереві
        public List<int> FindPath(int name) //де name значення вузла до якого потрібно знайти шлях
        {
            List<int> path = new List<int>();//тут будемо зберігати знайдений шлях
            TreeNode node = Root;//записуємо в початковий вузол корінь дерева
                                 //шукаємо шлях
            while (node != null && node.Name != name)//якшо поточний вузол не порожній, і значення поточного вузла не рівне шуканому продовжуємо пошук
            {
                path.Add(node.Name);//додаємо поточний вузол до шляху
                if (name < node.Name)//якщо шукане значення менше значення поточного вузла
                {
                    node = node.Left;//то переміщуємося в лівий зв'язаний вузол
                }
                else //якщо ні
                {
                    node = node.Right;//то переміщуємося в правий зв'язаний вузол
                }
            }
            if (node != null) //якщо в результаті пошуку вузол не порожній, то ми знайшли потрібний вузол дерева
            {
                path.Add(node.Name);//додаємо його до шляху
            }
            else //якщо порожній, то маршруту не існує
            {
                path.Clear();//очищуємо маршрут
            }
            return path;//повертаємо вузли через які проходить знайдений шлях
        }
    }
}
