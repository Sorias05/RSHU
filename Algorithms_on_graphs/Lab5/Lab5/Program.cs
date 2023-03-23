using System.Text;

namespace Lab5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            Graph graph = new Graph();
            //створюємо вершини 1-8
            Vertex v1 = new Vertex(1);
            Vertex v2 = new Vertex(2);
            Vertex v3 = new Vertex(3);
            Vertex v4 = new Vertex(4);
            Vertex v5 = new Vertex(5);
            Vertex v6 = new Vertex(6);
            Vertex v7 = new Vertex(7);
            Vertex v8 = new Vertex(8);
            //додаємо вершини в граф
            graph.AddVertex(v1);
            graph.AddVertex(v2);
            graph.AddVertex(v3);
            graph.AddVertex(v4);
            graph.AddVertex(v5);
            graph.AddVertex(v6);
            graph.AddVertex(v7);
            graph.AddVertex(v8);
            //додаемо ребра в раф (1;2)(1;4)(2;3)(2;5)(3;6)(4;5)(4;7)(5;6)(5;8)(6;9)(7;8)(8;9)
            graph.AddEdge(v1, v2);
            graph.AddEdge(v1, v3);
            graph.AddEdge(v1, v4);
            graph.AddEdge(v1, v7);
            graph.AddEdge(v2, v4);
            graph.AddEdge(v2, v5);
            graph.AddEdge(v2, v6);
            graph.AddEdge(v3, v5);
            graph.AddEdge(v3, v6);
            graph.AddEdge(v3, v7);
            graph.AddEdge(v4, v6);
            graph.AddEdge(v4, v7);
            graph.AddEdge(v5, v8);
            graph.AddEdge(v6, v8);
            graph.AddEdge(v7, v8);
            Console.WriteLine();
            Console.WriteLine("Найкоротший шлях (пошук в глибину) від 1 до 8 вершини");//виводимо рядок
            List<int> path = graph.DFS(1, 8); //вираховуємо найкоротший маршрут методом пошуку в глибину
            if (path.Count > 0)//якщо списку вершин вершини є
            {
                foreach (int p in path) Console.Write(p + " ");//тоді виводимо шлях
            }
            else
            { Console.WriteLine("Шляху від не існує"); }//якщо список порожній, шляху не існує
                                                        //чекаємо поки користувач натисне любу клавішу на клавіатурі
            Console.ReadKey();
        }
    }
}