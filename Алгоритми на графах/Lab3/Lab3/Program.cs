using Lab3;
using System.Text;

namespace Lab3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            //оголошуємо граф
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
            //додаемо ребра в граф, граф не орієнтований тому треба додати вершини попарно,
            //наприклад якщо зв'язок 1-3 з вагою 5, то ми маємо ї додати зв'язок 3-1 з вагою 5
            graph.AddEdge(v1, v2, 4);
            graph.AddEdge(v1, v4, 3);
            graph.AddEdge(v1, v3, 1);
            graph.AddEdge(v2, v1, 4);
            graph.AddEdge(v2, v3, 2);
            graph.AddEdge(v2, v5, 4);
            graph.AddEdge(v3, v1, 1);
            graph.AddEdge(v3, v2, 2);
            graph.AddEdge(v3, v6, 2);
            graph.AddEdge(v4, v1, 3);
            graph.AddEdge(v4, v7, 1);
            graph.AddEdge(v5, v2, 4);
            graph.AddEdge(v5, v6, 3);
            graph.AddEdge(v5, v7, 5);
            graph.AddEdge(v6, v3, 2);
            graph.AddEdge(v6, v5, 3);
            graph.AddEdge(v6, v8, 2);
            graph.AddEdge(v7, v4, 1);
            graph.AddEdge(v7, v5, 5);
            graph.AddEdge(v7, v8, 3);
            graph.AddEdge(v8, v6, 2);
            graph.AddEdge(v8, v7, 3);
            //вираховуємо найдешевші (найкоротші) шляхи обходу графу із заданої вершини
            int[] distances = graph.Dijkstra(6);
            //виведемо найкоротші (найдешевші) маршрути із вершини 6
            Console.WriteLine("Вершина\tВартість Маршрут");
            for (int i = 0; i < graph.VertexCount; i++)//перебираємо всі вершини
            {
                Console.Write((i + 1) + "\t" + distances[i] + " \t");//+1 бо в нас вершини починаються з 1ці, а масив з 0ля
                List<int> path = graph.GetPath_Dijkstra(i, 5, graph.prev);//визначаємо маршрут
                foreach (int v in path)//перебираємо всі вершини шляху і змінну v
                {
                    Console.Write(" " + (v + 1));//виводимо влідуючу вершину маршруту
                }
                Console.WriteLine();
            }
            //чекаємо поки користувач натисне любу клавішу на клавіатурі
            Console.ReadKey();
        }
    }
}