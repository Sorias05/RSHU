using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab5
{
    internal class Graph
    {
        //Списки для зберігання вершин та ребер
        List<Vertex> Vertexes = new List<Vertex>();
        List<Edge> Edges = new List<Edge>();
        //повертаємо кількість вершин графа
        public int VertexCount => Vertexes.Count;
        //повертаємо кількість ребер графа
        public int EdgeCount => Edges.Count;
        //додаємо вершину
        public void AddVertex(Vertex vertex)
        {
            Vertexes.Add(vertex);
        }
        //додаємо ребро
        public void AddEdge(Vertex from, Vertex to)
        {
            var edge = new Edge(from, to);
            Edges.Add(edge);
        }
        //Матриця суміжності
        public int[,] Adjacency_Matrix()
        {
            var matrix = new int[Vertexes.Count, Vertexes.Count];
            foreach (var edge in Edges)
            {
                var row = edge.From.Number;
                var column = edge.To.Number;
                matrix[row - 1, column - 1] = edge.Weight;// -1 бо в масиві елементи починаються із 0 а вершини графу з 1
            }
            return matrix;
        }
        //матриця інцидентності
        public int[,] Incidence_Matrix()
        {
            var matrix = new int[Vertexes.Count, Edges.Count];
            for (int i = 0; i < Edges.Count; i++)
            {
                matrix[Edges[i].From.Number - 1, i] = 1;// -1 бо в масиві елементи починаються із 0 а вершини графу з 1
                matrix[Edges[i].To.Number - 1, i] = 1;
            }
            return matrix;
        }
        //повертаємо вершину за його індексом
        public Vertex Vertex(int i)
        {
            return Vertexes[i];
        }
        //повертаємо ребро за його індексом
        public Edge Edge(int i)
        {
            return Edges[i];
        }
        public List<int>[] adjacency_list()
        {
            List<int>[] list = new List<int>[VertexCount]; //сюди помістимо результат
            for (int i = 0; i < VertexCount; i++) list[i] = new List<int>();//створюємо всі елементи списку
            foreach (Edge edge in Edges) list[edge.From.Number - 1].Add(edge.To.Number - 1);//додаємо в список зв'язок між вершинами
                                                                                            // -1 бо у нас вершини починаються з 1-ці а елементи списку з 0-ля
            return list;
        }
        //Пошук шляху від однієї вершини до іншої за допомогою алгоритму пошуку в ширину (BFS) Breadth First Search
        public List<int> BFS(int start, int dest)
        {
            start = start - 1; dest = dest - 1;//переходимо до нумерації вершин з 0, для правильної роботи алгоритму
            List<int>[] adj = adjacency_list();//формуємо список суміжності вершин графу
            bool[] visited = new bool[VertexCount]; //створюємо масив відвіданих вершин
            int[] parent = new int[VertexCount]; //створюємо масив вершин "батьків"
            for (int i = 0; i < VertexCount; i++) //задаємо масивам початкові значення
            {
                visited[i] = false;//жодну вершину ми ще не проходили
                parent[i] = -1;//в жодної вершини немає "батька"
            }
            Queue<int> q = new Queue<int>();//створюємо чергу, в яку будемо поміщати вершини які потрібно обійти
            visited[start] = true;//помічаємо початкову вершину відвіданою
            q.Enqueue(start);//додаємо її (початкову вершину) в чергу
            while (q.Count != 0) //поки ще лишилися елементи в черзі
            {
                int u = q.Dequeue();//виймаємо слідуючу вершину з черги і поміщаємо її у u
                foreach (int v in adj[u])//перебираємо всі вершини із списку суміжності графа через змінну v
                {
                    if (!visited[v]) //якщо в цій вершины ми ще не були
                    {
                        visited[v] = true; //помычаэмо її як відвідану
                        parent[v] = u;//додаємо батька (у вершину v ми можемо потрапити з вершини u)
                        q.Enqueue(v);//додаємо вершину в чергу, щоб її також опрацювати
                    }
                    if (v == dest) //якщо вершина є кінцевою
                    {
                        // Знайдено шуканий маршрут
                        List<int> path = new List<int>();//створюємо список, щоб в нього помістити наш маршрут
                        int curr = dest;//оголошуємо змінну для поточної вершини і задаємо їй значення кінцевої вершини
                        while (curr != -1)//поки існує батьківська вершина
                        {
                            path.Add(curr + 1);//переходимо до нашої нумерації вершин з 1
                            curr = parent[curr];//додаємо вершину до шляху
                        }
                        path.Reverse();//змінюємо маршрут на протилежний, бо в нас перша вершина кінцева, а остання перша
                        return path;//повертаємо маршрут
                    }
                }
            }
            // Шуканий маршрут не знайдено
            return null;
        }
        //додамо додання ребра із можливостю задання ваги (вартості) ребра
        public void AddEdge(Vertex from, Vertex to, int weight)
        {
            var edge = new Edge(from, to, weight);
            Edges.Add(edge);
        }
        public List<Tuple<int, int>>[] adjacency_list_weights()
        {
            List<Tuple<int, int>>[] adj = new List<Tuple<int, int>>[VertexCount];//сюди помістимо результат
            for (int i = 0; i < VertexCount; i++) adj[i] = new List<Tuple<int, int>>();//створюємо всі елементи списку
            foreach (Edge edge in Edges)
                adj[edge.From.Number - 1].Add(new Tuple<int, int>(edge.To.Number - 1, edge.Weight));//додаємо в список зв'язок між вершинами
                                                                                                    // -1 бо у нас вершини починаються з 1-ці а елементи списку з 0-ля
            return adj;//повертаємо список суміжності
        }
        //визначення вершини з мінімальною вартістю, наступної, вершини до якої найдешевше переміститися
        private int MinDistance(int[] distances, bool[] visited)//перший параметр масив відстаней, другий - масив відвіданих вершин
        {
            int minDistance = int.MaxValue;//задаємо мінімальне значення досить великим числом
            int minIndex = -1; //вершина -1 (такої вершини у графі не існує)
            for (int i = 0; i < VertexCount; i++)//перебираємо всі вершини
            {
                if (!visited[i]) //якщо в цій вершині ми не були
                    if (distances[i] <= minDistance)//якщо відстань менше мінімальної
                    {
                        minDistance = distances[i];//зберігаємо мінімальну вартість
                        minIndex = i;//зберігаємо індекс вершини
                    }
            }
            return minIndex;//повертаємо вершину до якої саме дешевше переміститися
        }
        public int[] prev; //тут зберігаємо попередні (батьківські вершини), щоб потім визначити по них шлях
        public int[] Dijkstra(int source)//розраховуємо наіменші шляхи по вартості до вершин із заданої алгоритмом Дейкстри
        {
            source = source - 1;//поправка, бо в нас вершини з 1, а у масиві з 0
            int[] distances = new int[VertexCount]; //створюємо масив ля збереження вартостей переміщення
            bool[] visited = new bool[VertexCount]; //створюємо масив відвіданих вершин графа
            List<Tuple<int, int>>[] adjacencyList = adjacency_list_weights(); //формуємо список суміжності описаний вище
            prev = new int[VertexCount];//в цьму масиві зберігаємо найдешевший маршрут
                                        // ініціалізація відстаней
            for (int i = 0; i < VertexCount; i++)//перебераємо відстані до кожної вершини
            {
                distances[i] = int.MaxValue;//заповнюємо відстані досить великим числом, щоб люба знайдена вартість переміщення була менше цого числа
            }
            distances[source] = 0;//задаємо вартість 0 для заданої вершини (вартість перемішення самої до себе)
                                  // знаходимо найдешевший шлях до всіх вершин
            for (int i = 0; i < VertexCount - 1; i++)//перебираємо всі вершини
            {
                int u = MinDistance(distances, visited);//вираховуємо мінімальну вартість до наступної вершини
                                                        //(на першому кроці буде початкова вершина бо вартість переміщення від неїх до неї 0)
                                                        //ця функція описана нижче
                visited[u] = true;//помічаємо її відвіданою
                foreach (Tuple<int, int> adjacency in adjacencyList[u])//перебираємо всі суміжні вершини з вершиною u
                {
                    int v = adjacency.Item1;//v - суміжна вершина
                    int weight = adjacency.Item2;//weight - вартість переміщення по ребру
                    if (!visited[v]) //ми не були у цій вершині
                        if (distances[u] != int.MaxValue) //якщо вартість до вершини у масиві відстаней вирахована
                            if (distances[u] + weight < distances[v]) //якщо знайдений шлях оптимальніший ніж вже існуючий
                            {
                                distances[v] = distances[u] + weight;//замінюємо значення знайденим
                                prev[v] = u;//зберігаємо посилання на попередню вершину, щоб визначити маршрут
                            }
                }
            }
            return distances;//повертаємо масив вартостей обходу вершин
        }
        //функція повертає найдешевший маршрут
        public List<int> GetPath_Dijkstra(int source, int target, int[] prev)
        //source - вершина до якої треба дійти, target - вершина з якої починаємо рух
        {
            List<int> path = new List<int>();//сюди збережемо маршрут
            int current = source;//поточна вершина = кінцевій вершині
            while (current != target)//поки поточна вершина не рівна кінцевій
            {
                path.Add(current);//додаємо поточну вершину до маршруту
                current = prev[current];//міняємо поточну вершину на батьківську
            }
            path.Add(target);//додаємо до шляху кінцеву вершину
            path.Reverse();//змінюємо порядок шляху, він в нас обернений
            return path;//повертаємо шлях
        }
        public List<int> DFS(int start, int end)//пошук в глибину start вершина з якої починаємо іти end - кінцева
        {
            start = start - 1; end = end - 1;////переходимо до нумерації вершин з 0, для правильної роботи алгоритму
            bool[] visited = new bool[VertexCount];//створюємо масив відвіданих вершин
            int[] parent = new int[VertexCount];//створюємо масив вершин "батьків"
            List<int>[] adj = adjacency_list();//формуємо список суміжності вершин графу
            Stack<int> stack = new Stack<int>();//створюємо стек, аналог черги, але формується в зворотньому порядку
            visited[start] = true;//задаємо що початкову вкпшину відвідано
            stack.Push(start);//додаємо її до черги, як початкову
            while (stack.Count > 0)//поки в стеку ще є елементи
            {
                int v = stack.Pop();//беремо елемент зі стеку у v
                if (v == end)//якщо наступний елемент стеку рівний кінцівій вершині
                {
                    break;//перериваємо роботу функції
                }
                foreach (int i in adj[v])//перебираємо список суміжності графа
                {
                    if (!visited[i])//якщо вершина не опрацьована
                    {
                        visited[i] = true;//помічаємо її, як відвідану
                        parent[i] = v;//додаємо посилання на неї в масив батьків
                        stack.Push(i);//додаємо вершину у стек, щоб опрацювати
                    }
                }
            }
            List<int> path = new List<int>();//створимо список, в який помістимо шлях
            if (!visited[end])//якщо кінцева вершина не помічена як ваідвідана
            {
                return path;//шляху не існує повертаємо пустий список
            }
            for (int i = end; i != start; i = parent[i]) //перебираємо з кінцевої вершини, поки вона не буде рівною початковій, переміщуючись по масиву батьків
            {
                path.Add(i + 1);//додаємо вершину до маршруту, +1 тому, що в нашому графі вершини починаються із 1
            }
            path.Add(start + 1);//додаємо до маршруту початкову вершину +1, це поправка на нумерацію
            path.Reverse();//шлях в нас зформувався в зворотньому порядку, тому обертаємо маршрут
            return path;//повертаємо одержаний маршрут
        }
    }
}
