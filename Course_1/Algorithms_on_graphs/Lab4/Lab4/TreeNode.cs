using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    internal class TreeNode
    {
        public TreeNode Left; //посилання на лівий зв'язаний вузол
        public TreeNode Right; //посилання на правий з'язаний вузол
        public int Name;//назва вузла
        public TreeNode(int name) //конструктор вузла, name - значення вузла (наприклад номер)
        {
            Name = name;//задаємо значення вузлу
            Left = null;//вказуємо що переходу до слідуючого лівого вузла немає
            Right = null;//вказуємо що переходу до слідуючого правого вузла немає
                         //вони будуть задаватися в процесі створення самого дерева а не вузла
        }
    }
}
