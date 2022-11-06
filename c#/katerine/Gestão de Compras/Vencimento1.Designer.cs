namespace Gestão_de_Compras
{
    partial class Vencimento1
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
            this.lblVencimento1 = new System.Windows.Forms.Label();
            this.dgvVenci1 = new System.Windows.Forms.DataGridView();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVenci1)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.lblVencimento1);
            this.panel1.Controls.Add(this.dgvVenci1);
            this.panel1.Location = new System.Drawing.Point(19, 46);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(423, 248);
            this.panel1.TabIndex = 0;
            // 
            // lblVencimento1
            // 
            this.lblVencimento1.AutoSize = true;
            this.lblVencimento1.Location = new System.Drawing.Point(290, 191);
            this.lblVencimento1.Name = "lblVencimento1";
            this.lblVencimento1.Size = new System.Drawing.Size(106, 13);
            this.lblVencimento1.TabIndex = 1;
            this.lblVencimento1.Text = "Vencimento em 1 dia";
            // 
            // dgvVenci1
            // 
            this.dgvVenci1.AllowUserToAddRows = false;
            this.dgvVenci1.AllowUserToDeleteRows = false;
            this.dgvVenci1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvVenci1.Location = new System.Drawing.Point(15, 17);
            this.dgvVenci1.Name = "dgvVenci1";
            this.dgvVenci1.ReadOnly = true;
            this.dgvVenci1.Size = new System.Drawing.Size(381, 150);
            this.dgvVenci1.TabIndex = 0;
            this.dgvVenci1.DataSourceChanged += new System.EventHandler(this.dgvVenci1_DataSourceChanged);
            // 
            // Vencimento1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(454, 363);
            this.Controls.Add(this.panel1);
            this.Name = "Vencimento1";
            this.Text = "Vencimento em 1 dia";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVenci1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label lblVencimento1;
        private System.Windows.Forms.DataGridView dgvVenci1;
    }
}