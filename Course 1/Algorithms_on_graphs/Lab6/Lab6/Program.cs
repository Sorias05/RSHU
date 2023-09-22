namespace Lab6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
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
            //додаемо ребра в граф, граф не орієнтований але ми не будемо додати вершини попарно,
            //викристаємо функцію яка автоматично це зробить, ми її додали як adjacency_list_unoriented()
            graph.AddEdge(v1, v2);
            graph.AddEdge(v1, v3);
            graph.AddEdge(v1, v4);
            graph.AddEdge(v1, v5);
            graph.AddEdge(v2, v3);
            graph.AddEdge(v2, v4);
            graph.AddEdge(v2, v5);
            graph.AddEdge(v3, v4);
            graph.AddEdge(v3, v6);
            graph.AddEdge(v4, v7);
            graph.AddEdge(v5, v6);
            graph.AddEdge(v5, v7);
            graph.AddEdge(v6, v7);
            graph.AddEdge(v6, v8);
            graph.AddEdge(v7, v8);

            int[] colors = graph.colorGraph(); //Розфарбовуємо граф
            Console.WriteLine("Вершина\tКолір");//виводимо заголовок таблиці
            for (int i = 0; i < graph.VertexCount; i++)//і від 0 до кількості елементів розфарбованого масиву
                Console.WriteLine((i + 1) + "\t" + colors[i]);//виводимо вершину і її колір +1 бо в нас вершини починаються із 1-ці
            Console.WriteLine();//відступаємо один рядок донизу
                                //максимальний індекс кольору графу і буде хроматичним числом
            int chromaticNumber = 0;//встановлюємо 0 як початкове хроматичне число
            for (int i = 0; i < graph.VertexCount; i++)//перебираємо весь масив розфарбованих вершин
                chromaticNumber = Math.Max(chromaticNumber, colors[i]);//якщо наступний індекс кольору більший за хроматичне число, то оновлюємо його Console.WriteLine("Хроматичне число графа: "+chromaticNumber);//виводимо хроматичне число графу
            Console.WriteLine("Хроматичне число графа: " + chromaticNumber);//виводимо хроматичне число графу

            Console.ReadKey();
        }
    }
}