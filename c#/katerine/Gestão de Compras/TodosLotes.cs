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
    public partial class TodosLotes : Form
    {
        private TodosLotes()
        {
            InitializeComponent();
            dataGridView1.DataSource = BancoDeDados.Compras;
        }
        private static TodosLotes instance { get; set; }
        public static TodosLotes GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new TodosLotes();
            }
            return instance;
        }
        private void TodosLotes_Load(object sender, EventArgs e)
        {

        }
    }
}
