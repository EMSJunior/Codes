using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Gestão_de_Compras
{
    public partial class TodosOsLotes : Form
    {
        public TodosOsLotes()
        {
            InitializeComponent();
            dataGridView1.DataSource = BancoDeDados.Compras;
        }
        public static TodosOsLotes instance { get; set; }
        public static TodosOsLotes  GetInstance()
        {
            if (instance == null
                || instance.IsDisposed)
            {
                instance = new TodosOsLotes();
            }
            return instance;
        }
    }
}
