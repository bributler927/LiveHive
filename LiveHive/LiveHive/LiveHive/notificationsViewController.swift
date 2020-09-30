//
//  notificationsViewController.swift
//  LiveHive
//
//  Created by Brianna Butler on 9/29/20.
//  Copyright © 2020 LiveHive. All rights reserved.
//

import UIKit

class notificationsViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var notificationTable:
        UITableView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        notificationTable.register(UITableViewCell.self, forCellReuseIdentifier: "notifCell")
        notificationTable.dataSource = self
        notificationTable.delegate = self
        
        
        // Do any additional setup after loading the view.
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
           
        }

        func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return 1
        }

        func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
            let cell = tableView.dequeueReusableCell(withIdentifier: "notifCell", for: indexPath as IndexPath)
            
            return cell
        }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection
                                section: Int) -> String? {
        let date = Date()
        let formatter = DateFormatter()
        
        formatter.dateFormat = "MM dd"
        
        let result = formatter.string(from: date)
        
       return result
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
