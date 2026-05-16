import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  TextInput,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const ProfileScreen = () => {
  const [profileData, setProfileData] = useState({
    name: 'Nabin',
    email: 'nabin@lingora.com',
  });
  const [isEditing, setIsEditing] = useState(false);

  const stats = {
    streak: 14,
    xp: 1250,
    gems: 350,
    hearts: 5,
  };

  const languages = [
    { name: 'Sanskrit', progress: 0.6 },
    { name: 'Spanish', progress: 0.2 },
  ];

  const achievements = [
    { id: 1, title: '7 Day Streak', icon: 'flame', earned: true },
    { id: 2, title: '30 Day Streak', icon: 'flame', earned: false },
    { id: 3, title: 'Perfect Lesson', icon: 'star', earned: true },
    { id: 4, title: '100 XP', icon: 'trophy', earned: true },
    { id: 5, title: '500 XP', icon: 'trophy', earned: false },
    { id: 6, title: 'Night Owl', icon: 'moon', earned: false },
  ];

  const settings = [
    { id: 1, title: 'Notifications', icon: 'notifications' },
    { id: 2, title: 'Dark Mode', icon: 'moon' },
    { id: 3, title: 'Audio Quality', icon: 'volume-high' },
    { id: 4, title: 'Help & Support', icon: 'help-circle' },
  ];

  const handleInputChange = (field, value) => {
    setProfileData(prev => ({ ...prev, [field]: value }));
  };

  const handleSave = () => {
    setIsEditing(false);
  };

  return (
    <ScrollView style={styles.container} showsVerticalScrollIndicator={false}>
      <View style={styles.header}>
        <View style={styles.avatarContainer}>
          <Ionicons name="person-circle" size={80} color="#6C63FF" />
          {isEditing && (
            <TouchableOpacity style={styles.editAvatarBtn}>
              <Ionicons name="camera" size={16} color="#fff" />
            </TouchableOpacity>
          )}
        </View>

        {isEditing ? (
          <View style={styles.editFields}>
            <TextInput
              style={styles.nameInput}
              value={profileData.name}
              onChangeText={text => handleInputChange('name', text)}
              placeholder="Your name"
            />
            <TextInput
              style={styles.emailInput}
              value={profileData.email}
              onChangeText={text => handleInputChange('email', text)}
              placeholder="Email"
              keyboardType="email-address"
            />
            <TouchableOpacity style={styles.saveBtn} onPress={handleSave}>
              <Text style={styles.saveBtnText}>Save</Text>
            </TouchableOpacity>
          </View>
        ) : (
          <View style={styles.userInfo}>
            <Text style={styles.userName}>{profileData.name}</Text>
            <Text style={styles.userEmail}>{profileData.email}</Text>
            <TouchableOpacity
              style={styles.editBtn}
              onPress={() => setIsEditing(true)}
            >
              <Text style={styles.editBtnText}>Edit Profile</Text>
            </TouchableOpacity>
          </View>
        )}
      </View>

      <View style={styles.statsCard}>
        <View style={styles.statItem}>
          <Ionicons name="flame" size={28} color="#FF9600" />
          <Text style={styles.statValue}>{stats.streak}</Text>
          <Text style={styles.statLabel}>Day Streak</Text>
        </View>
        <View style={styles.statDivider} />
        <View style={styles.statItem}>
          <Ionicons name="flash" size={28} color="#FFD700" />
          <Text style={styles.statValue}>{stats.xp}</Text>
          <Text style={styles.statLabel}>XP</Text>
        </View>
        <View style={styles.statDivider} />
        <View style={styles.statItem}>
          <Ionicons name="diamond" size={28} color="#1CB0F6" />
          <Text style={styles.statValue}>{stats.gems}</Text>
          <Text style={styles.statLabel}>Gems</Text>
        </View>
        <View style={styles.statDivider} />
        <View style={styles.statItem}>
          <Ionicons name="heart" size={28} color="#FF4B4B" />
          <Text style={styles.statValue}>{stats.hearts}</Text>
          <Text style={styles.statLabel}>Hearts</Text>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>My Languages</Text>
        {languages.map((lang, index) => (
          <View key={index} style={styles.languageCard}>
            <Ionicons name="language" size={32} color="#6C63FF" />
            <View style={styles.languageInfo}>
              <Text style={styles.languageName}>{lang.name}</Text>
              <View style={styles.progressBar}>
                <View
                  style={[
                    styles.progressFill,
                    { width: `${lang.progress * 100}%` },
                  ]}
                />
              </View>
              <Text style={styles.progressText}>
                {Math.round(lang.progress * 100)}% complete
              </Text>
            </View>
          </View>
        ))}
        <TouchableOpacity style={styles.addLanguageBtn}>
          <Ionicons name="add" size={20} color="#6C63FF" />
          <Text style={styles.addLanguageText}>Add Language</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Achievements</Text>
        <View style={styles.badgesGrid}>
          {achievements.map(item => (
            <View
              key={item.id}
              style={[
                styles.badgeItem,
                !item.earned && styles.badgeLocked,
              ]}
            >
              <Ionicons
                name={item.icon}
                size={32}
                color={item.earned ? '#6C63FF' : '#ccc'}
              />
              <Text
                style={[
                  styles.badgeTitle,
                  !item.earned && styles.badgeLockedText,
                ]}
              >
                {item.title}
              </Text>
            </View>
          ))}
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Settings</Text>
        {settings.map(item => (
          <TouchableOpacity key={item.id} style={styles.settingsRow}>
            <Ionicons name={item.icon} size={24} color="#666" />
            <Text style={styles.settingsText}>{item.title}</Text>
            <Ionicons name="chevron-forward" size={20} color="#ccc" />
          </TouchableOpacity>
        ))}
      </View>

      <TouchableOpacity style={styles.logoutBtn}>
        <Ionicons name="log-out" size={20} color="#FF4B4B" />
        <Text style={styles.logoutText}>Logout</Text>
      </TouchableOpacity>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7F7F7',
  },
  header: {
    alignItems: 'center',
    backgroundColor: '#fff',
    paddingVertical: 30,
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
    marginBottom: 16,
  },
  avatarContainer: {
    position: 'relative',
  },
  editAvatarBtn: {
    position: 'absolute',
    bottom: 0,
    right: 0,
    backgroundColor: '#6C63FF',
    width: 24,
    height: 24,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
  },
  userInfo: {
    alignItems: 'center',
    marginTop: 10,
  },
  userName: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#333',
  },
  userEmail: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  editBtn: {
    marginTop: 10,
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#6C63FF',
  },
  editBtnText: {
    color: '#6C63FF',
    fontWeight: '600',
    fontSize: 14,
  },
  editFields: {
    width: '80%',
    marginTop: 10,
  },
  nameInput: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    padding: 10,
    marginBottom: 10,
    fontSize: 16,
  },
  emailInput: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    padding: 10,
    marginBottom: 10,
    fontSize: 16,
  },
  saveBtn: {
    backgroundColor: '#6C63FF',
    padding: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  saveBtnText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  statsCard: {
    flexDirection: 'row',
    backgroundColor: '#fff',
    marginHorizontal: 16,
    borderRadius: 12,
    padding: 16,
    elevation: 2,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 4,
    marginBottom: 16,
  },
  statItem: {
    flex: 1,
    alignItems: 'center',
  },
  statValue: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 4,
  },
  statLabel: {
    fontSize: 10,
    color: '#777',
    marginTop: 2,
  },
  statDivider: {
    width: 1,
    backgroundColor: '#eee',
  },
  section: {
    backgroundColor: '#fff',
    marginHorizontal: 16,
    marginBottom: 16,
    borderRadius: 12,
    padding: 16,
    elevation: 2,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 4,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },
  languageCard: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  languageInfo: {
    flex: 1,
    marginLeft: 12,
  },
  languageName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
  },
  progressBar: {
    height: 6,
    backgroundColor: '#eee',
    borderRadius: 3,
    marginVertical: 4,
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#6C63FF',
    borderRadius: 3,
  },
  progressText: {
    fontSize: 12,
    color: '#888',
  },
  addLanguageBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
    borderWidth: 1,
    borderColor: '#6C63FF',
    borderRadius: 8,
    marginTop: 4,
  },
  addLanguageText: {
    color: '#6C63FF',
    fontWeight: '600',
    marginLeft: 6,
  },
  badgesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  badgeItem: {
    width: '30%',
    alignItems: 'center',
    marginBottom: 16,
    marginRight: '3%',
  },
  badgeLocked: {
    opacity: 0.5,
  },
  badgeTitle: {
    fontSize: 11,
    color: '#333',
    marginTop: 4,
    textAlign: 'center',
  },
  badgeLockedText: {
    color: '#aaa',
  },
  settingsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  settingsText: {
    flex: 1,
    fontSize: 16,
    color: '#333',
    marginLeft: 12,
  },
  logoutBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginHorizontal: 16,
    marginBottom: 30,
    paddingVertical: 14,
    backgroundColor: '#fff',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#FFE0E0',
  },
  logoutText: {
    color: '#FF4B4B',
    fontWeight: '600',
    fontSize: 16,
    marginLeft: 8,
  },
});

export default ProfileScreen;