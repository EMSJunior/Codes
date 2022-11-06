namespace Gestão_de_Compras
{
    partial class VencimentoUm
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
            this.dgvVencimentoUm = new System.Windows.Forms.DataGridView();
            this.lblVencimentoEmUmDia = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVencimentoUm)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvVencimentoUm
            // 
            this.dgvVencimentoUm.AllowUserToAddRows = false;
            this.dgvVencimentoUm.AllowUserToDeleteRows = false;
            this.dgvVencimentoUm.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvVencimentoUm.Location = new System.Drawing.Point(2, 0);
            this.dgvVencimentoUm.Name = "dgvVencimentoUm";
            this.dgvVencimentoUm.ReadOnly = true;
            this.dgvVencimentoUm.Size = new System.Drawing.Size(410, 248);
            this.dgvVencimentoUm.TabIndex = 0;
            // 
            // lblVencimentoEmUmDia
            // 
            this.lblVencimentoEmUmDia.AutoSize = true;
            this.lblVencimentoEmUmDia.Location = new System.Drawing.Point(306, 281);
            this.lblVencimentoEmUmDia.Name = "lblVencimentoEmUmDia";
            this.lblVencimentoEmUmDia.Size = new System.Drawing.Size(114, 13);
            this.lblVencimentoEmUmDia.TabIndex = 1;
            this.lblVencimentoEmUmDia.Text = "Venciemnto em um dia";
            // 
            // VencimentoUm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(580, 325);
            this.Controls.Add(this.lblVencimentoEmUmDia);
            this.Controls.Add(this.dgvVencimentoUm);
            this.Name = "VencimentoUm";
            this.Text = "VencimentoUm";
            ((System.ComponentModel.ISupportInitialize)(this.dgvVencimentoUm)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvVencimentoUm;
        private System.Windows.Forms.Label lblVencimentoEmUmDia;
    }
}