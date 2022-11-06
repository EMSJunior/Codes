namespace Gestão_de_Compras
{
    partial class VencimentoPersonalizado
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.txtVencimento1 = new System.Windows.Forms.TextBox();
            this.lblVencimentoP = new System.Windows.Forms.Label();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.txtVencimento1);
            this.panel1.Controls.Add(this.lblVencimentoP);
            this.panel1.Controls.Add(this.dataGridView1);
            this.panel1.Location = new System.Drawing.Point(16, 30);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(474, 267);
            this.panel1.TabIndex = 0;
            // 
            // txtVencimento1
            // 
            this.txtVencimento1.Location = new System.Drawing.Point(358, 174);
            this.txtVencimento1.Name = "txtVencimento1";
            this.txtVencimento1.Size = new System.Drawing.Size(100, 20);
            this.txtVencimento1.TabIndex = 2;
            this.txtVencimento1.TextChanged += new System.EventHandler(this.txtVencimento1_TextChanged);
            // 
            // lblVencimentoP
            // 
            this.lblVencimentoP.AutoSize = true;
            this.lblVencimentoP.Location = new System.Drawing.Point(256, 177);
            this.lblVencimentoP.Name = "lblVencimentoP";
            this.lblVencimentoP.Size = new System.Drawing.Size(83, 13);
            this.lblVencimentoP.TabIndex = 1;
            this.lblVencimentoP.Text = "Vencimento em:";
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.AllowUserToDeleteRows = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(14, 12);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.ReadOnly = true;
            this.dataGridView1.Size = new System.Drawing.Size(444, 150);
            this.dataGridView1.TabIndex = 0;
            // 
            // VencimentoPersonalizado
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(506, 333);
            this.Controls.Add(this.panel1);
            this.Name = "VencimentoPersonalizado";
            this.Text = "Vencimento Personalizado";
            this.Load += new System.EventHandler(this.VencimentoPersonalizado_Load);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.TextBox txtVencimento1;
        private System.Windows.Forms.Label lblVencimentoP;
        private System.Windows.Forms.DataGridView dataGridView1;
    }
}