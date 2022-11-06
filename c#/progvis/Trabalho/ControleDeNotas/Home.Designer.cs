namespace ControleDeNotas
{
    partial class Home
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.programaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.btnSobre = new System.Windows.Forms.ToolStripMenuItem();
            this.btnSair = new System.Windows.Forms.ToolStripMenuItem();
            this.cadrastosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.btnNewNota = new System.Windows.Forms.ToolStripMenuItem();
            this.relatóriosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.btnLotes = new System.Windows.Forms.ToolStripMenuItem();
            this.btn1dia = new System.Windows.Forms.ToolStripMenuItem();
            this.btn5dias = new System.Windows.Forms.ToolStripMenuItem();
            this.btnVenci = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.programaToolStripMenuItem,
            this.cadrastosToolStripMenuItem,
            this.relatóriosToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(800, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // programaToolStripMenuItem
            // 
            this.programaToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnSobre,
            this.btnSair});
            this.programaToolStripMenuItem.Name = "programaToolStripMenuItem";
            this.programaToolStripMenuItem.Size = new System.Drawing.Size(71, 20);
            this.programaToolStripMenuItem.Text = "Programa";
            // 
            // btnSobre
            // 
            this.btnSobre.Name = "btnSobre";
            this.btnSobre.Size = new System.Drawing.Size(180, 22);
            this.btnSobre.Text = "Sobre";
            this.btnSobre.Click += new System.EventHandler(this.btnSobre_Click);
            // 
            // btnSair
            // 
            this.btnSair.Name = "btnSair";
            this.btnSair.Size = new System.Drawing.Size(180, 22);
            this.btnSair.Text = "Sair";
            this.btnSair.Click += new System.EventHandler(this.btnSair_Click);
            // 
            // cadrastosToolStripMenuItem
            // 
            this.cadrastosToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnNewNota});
            this.cadrastosToolStripMenuItem.Name = "cadrastosToolStripMenuItem";
            this.cadrastosToolStripMenuItem.Size = new System.Drawing.Size(71, 20);
            this.cadrastosToolStripMenuItem.Text = "Cadrastos";
            // 
            // btnNewNota
            // 
            this.btnNewNota.Name = "btnNewNota";
            this.btnNewNota.Size = new System.Drawing.Size(170, 22);
            this.btnNewNota.Text = "Lançar Nota Fiscal";
            this.btnNewNota.Click += new System.EventHandler(this.btnNewNota_Click);
            // 
            // relatóriosToolStripMenuItem
            // 
            this.relatóriosToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnLotes,
            this.btn1dia,
            this.btn5dias,
            this.btnVenci});
            this.relatóriosToolStripMenuItem.Name = "relatóriosToolStripMenuItem";
            this.relatóriosToolStripMenuItem.Size = new System.Drawing.Size(71, 20);
            this.relatóriosToolStripMenuItem.Text = "Relatórios";
            // 
            // btnLotes
            // 
            this.btnLotes.Name = "btnLotes";
            this.btnLotes.Size = new System.Drawing.Size(213, 22);
            this.btnLotes.Text = "Todos os Lotes";
            this.btnLotes.Click += new System.EventHandler(this.btnLotes_Click);
            // 
            // btn1dia
            // 
            this.btn1dia.Name = "btn1dia";
            this.btn1dia.Size = new System.Drawing.Size(213, 22);
            this.btn1dia.Text = "Vencimento em até 1 dia";
            this.btn1dia.Click += new System.EventHandler(this.btn1dia_Click);
            // 
            // btn5dias
            // 
            this.btn5dias.Name = "btn5dias";
            this.btn5dias.Size = new System.Drawing.Size(213, 22);
            this.btn5dias.Text = "Vencimento em até 5 dias";
            this.btn5dias.Click += new System.EventHandler(this.btn5dias_Click);
            // 
            // btnVenci
            // 
            this.btnVenci.Name = "btnVenci";
            this.btnVenci.Size = new System.Drawing.Size(213, 22);
            this.btnVenci.Text = "Vencimento Personalizado";
            this.btnVenci.Click += new System.EventHandler(this.btnVenci_Click);
            // 
            // Home
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Home";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Controle de Vencimentos";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem programaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem btnSobre;
        private System.Windows.Forms.ToolStripMenuItem btnSair;
        private System.Windows.Forms.ToolStripMenuItem cadrastosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem btnNewNota;
        private System.Windows.Forms.ToolStripMenuItem relatóriosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem btnLotes;
        private System.Windows.Forms.ToolStripMenuItem btn1dia;
        private System.Windows.Forms.ToolStripMenuItem btn5dias;
        private System.Windows.Forms.ToolStripMenuItem btnVenci;
    }
}

