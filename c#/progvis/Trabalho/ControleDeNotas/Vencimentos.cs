using Gestão_de_Compras;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControleDeNotas
{
    public partial class Vencimentos : Form
    {
        private Vencimentos()
        {
            InitializeComponent();
        }

        private static Vencimentos instanceUm { get; set; }
        private static Vencimentos instanceCinco { get; set; }
        private static Vencimentos instance { get; set; }
        public static Vencimentos GetInstance(Int16 n = 2) // Valor 2 para acessar o Default
        {
            switch (n)
            {
                // Faz uma seleção de jalenas para com apenas uma janela eu ter acesso a todos as funcionalidades
                case 1:
                    if (instanceUm == null || instanceUm.IsDisposed)
                    {
                        instanceUm = new Vencimentos();
                        instanceUm.Text = "Vencimentos nos proxímos um dia";
                    }
                    instanceUm.dtpInicio.Value = DateTime.Now;
                    instanceUm.dtpFinal.Value = DateTime.Now.AddDays(1);
                    instanceUm.F5();

                    return instanceUm;

                case 5:
                    if (instanceCinco == null || instanceCinco.IsDisposed)
                    {
                        instanceCinco = new Vencimentos();
                        instanceCinco.Text = "Vencimentos nos proxímos cinco dias";

                    }
                    instanceCinco.dtpInicio.Value = DateTime.Now;
                    instanceCinco.dtpFinal.Value = DateTime.Now.AddDays(5);
                    instanceCinco.F5();

                    return instanceCinco;

                case -1: // Valor -1 significa que são todos os dias
                    if (instance == null || instance.IsDisposed)
                    {
                        instance = new Vencimentos();

                    }
                    instance.TodosOsLotes();

                    return instance;

                default:
                    // Com intervalo personalizado, o usuario pode colocar quantos intervalos ele quiser
                    return new Vencimentos();
            }
            
        }
        
        public void F5()
        {
            if (dtpFinal.Value.Date >= dtpInicio.Value.Date)
            {
                List<Compra> notas = new List<Compra>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento.Date >= dtpInicio.Value.Date) && compra.Vencimento.Date <= dtpFinal.Value.Date)
                    {
                       notas.Add(compra);
                    }
                }
                
                
                dgvVencimentos.DataSource = notas;
                dgvVencimentos.Refresh();
            }
            else 
            {
                MessageBox.Show("Insira a data final maior que a de inicio !", "Erro");
            }
            
        }

        private void dtpInicio_ValueChanged(object sender, EventArgs e)
        {
            F5();
        }

        private void dtpFinal_ValueChanged(object sender, EventArgs e)
        {
            F5();
        }

        private void btnAll_Click(object sender, EventArgs e)
        {
            TodosOsLotes();
        }

        private void TodosOsLotes()
        {
            dgvVencimentos.DataSource = BancoDeDados.Compras;

        }

    }
}
