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
    public partial class Vencimento5 : Form
    {
        private Vencimento5()
        {
            InitializeComponent();
            try
            {
                List<Compra> notas = new List<Compra>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= 5)
                    {
                        notas.Add(compra);
                    }
                }

                dgvVenci5.DataSource = notas;
                dgvVenci5.Refresh();
            }
            catch { }
        }
        private static Vencimento5 instance { get; set; }
        public static Vencimento5 GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new Vencimento5();
            }
            return instance;
        }
       
    }
}
